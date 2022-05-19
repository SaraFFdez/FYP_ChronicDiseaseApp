import 'dart:html';

import 'package:flutter/material.dart';

class AnalysisPage extends StatefulWidget {
  const AnalysisPage({Key? key}) : super(key: key);

  @override
  State<AnalysisPage> createState() => _AnalysisPageState();
}

class _AnalysisPageState extends State<AnalysisPage> {
  List<String> activities = [];
  List<String> symptoms = [
    "Nausea",
    "Bloating",
    "Headaches",
    "Digestive issues"
  ];
  Map<String, List<String>> foodDiary = {
    "morning": ["Avocado", "Toast", "Eggs"],
    "afternoon": ["Pasta", "Cheese"],
    "evening": ["Soup", "Peas"],
    "no_time": ["Smoothie"]
  };
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.grey[100],
      body: Padding(
        padding: const EdgeInsets.all(15.0),
        child: Column(children: [
          Row(
            children: const [
              Text("Symptoms graph"),
              SizedBox(width: 40.0),
              Icon(Icons.settings, color: Colors.black)
            ],
          ),
          Column(
            children: [
              const Padding(
                padding: EdgeInsets.all(8.0),
                child: Text(
                  'Symptoms experienced today',
                  style: TextStyle(fontSize: 16.0, fontWeight: FontWeight.bold),
                ),
              ),
              Container(
                  margin: const EdgeInsets.fromLTRB(30, 0, 30, 10),
                  child: Table(
                      defaultVerticalAlignment:
                          TableCellVerticalAlignment.middle,
                      children: [...buildAllRows(symptoms)]))
            ],
          ),
          Row(
            children: const [
              Text("Food diary"),
              SizedBox(width: 40.0),
              Icon(Icons.settings, color: Colors.black)
            ],
          ),
          Container(
              margin: const EdgeInsets.all(15.0),
              child: Table(
                  defaultVerticalAlignment: TableCellVerticalAlignment.middle,
                  border: const TableBorder(
                      horizontalInside:
                          BorderSide(width: 1.0, color: Colors.black),
                      verticalInside:
                          BorderSide(width: 1.0, color: Colors.black)),
                  children: [
                    buildRow(["Morning", "Afternoon", "Evening", "Undet. time"],
                        isHeader: true),
                    ...buildAllRowsFood(foodDiary),
                  ])),
          Row(
            children: const [
              Text("Activity log"),
              SizedBox(width: 40.0),
              Icon(Icons.settings, color: Colors.black)
            ],
          ),
          Column(
            children: [
              const Padding(
                padding: EdgeInsets.all(8.0),
                child: Text(
                  'Activities done today',
                  style: TextStyle(fontSize: 16.0, fontWeight: FontWeight.bold),
                ),
              ),
              Container(
                  margin: const EdgeInsets.fromLTRB(30, 0, 30, 10),
                  child: Table(
                      defaultVerticalAlignment:
                          TableCellVerticalAlignment.middle,
                      children: [...buildAllRows(activities)]))
            ],
          )
        ]),
      ),
    );
  }

  TableRow buildRow(List<String> cells, {bool isHeader = false}) => TableRow(
          children: cells.map((cell) {
        final txtStyle = TextStyle(
            fontWeight: isHeader ? FontWeight.bold : FontWeight.normal,
            fontSize: isHeader ? 16.0 : 14.0);
        return Padding(
          padding: const EdgeInsets.all(4.0),
          child: Center(child: Text(cell, style: txtStyle)),
        );
      }).toList());

  List<TableRow> buildAllRows(List<String> array) {
    List<TableRow> rows = [];

    if (array.isEmpty) {
      return [
        buildRow(["None found"])
      ];
    } else if (array.length.remainder(2) == 1) {
      array.add(" ");
    }

    for (var i = 0; i < array.length; i = i + 2) {
      rows.add(buildRow([array[i], array[i + 1]]));
    }
    return rows;
  }

  List<TableRow> buildAllRowsFood(Map<String, List<String>> map) {
    List<TableRow> rows = [];

    if (map.isEmpty) {
      return [
        buildRow(["None found", "None found", "None found", "None found"])
      ];
    }
    var newMap = mapSameLength(map);
    var nullCheckList = newMap["morning"] ?? [];
    var maxLength = nullCheckList.length;
    if (maxLength == 0) {
      return [
        buildRow(["Error", "Error", "Error", "Error"])
      ];
    }
    var keys = map.keys;
    var errorList = List.filled(maxLength, "Error");
    for (var i = 0; i < maxLength; i++) {
      List<String> row = [];
      for (var key in keys) {
        var list = newMap[key] ?? errorList;

        row.add(list[i]);
      }
      rows.add(buildRow(row));
    }

    return rows;
  }

  //ASSUME ITS ALL SAME LENGTH FOR NOW
  Map<String, List<String>> mapSameLength(Map<String, List<String>> map) {
    Map<String, List<String>> newMap = {
      "morning": [],
      "afternoon": [],
      "evening": [],
      "no_time": []
    };
    var keys = map.keys;
    int maxLength = 0;
    for (var key in keys) {
      var list = map[key] ?? []; //checking for null.
      if (maxLength < list.length) {
        maxLength = list.length;
      }
    }
    if (maxLength == 0) {
      return newMap;
    }
    for (var key in keys) {
      var list = map[key] ?? []; //checking for null.
      if (maxLength > list.length) {
        var difference = maxLength - list.length;
        for (var i = 0; i < difference; i++) {
          list.add(" ");
        }
      }
      newMap[key] = list;
    }
    return newMap;
  }
}
