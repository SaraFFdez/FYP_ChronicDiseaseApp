import 'package:flutter/material.dart';

class AnalysisPage extends StatefulWidget {
  const AnalysisPage({Key? key}) : super(key: key);

  @override
  State<AnalysisPage> createState() => _AnalysisPageState();
}

class _AnalysisPageState extends State<AnalysisPage> {
  List<String> activities = ["go for a walk", "go to school", "relax"];
  List<String> symptoms = [
    "nausea",
    "bloating",
    "headaches",
    "digestive issues"
  ];
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
                      //defaultColumnWidth: ,
                      // border: TableBorder.all(
                      //     color: Colors.black, style: BorderStyle.solid, width: 1),
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
                  //defaultColumnWidth: ,
                  // border: TableBorder.all(
                  //     color: Colors.black, style: BorderStyle.solid, width: 1),
                  border: const TableBorder(
                      // right: BorderSide(width: 1.0, color: Colors.black),
                      // left: BorderSide(width: 1.0, color: Colors.black),
                      horizontalInside:
                          BorderSide(width: 1.0, color: Colors.black),
                      verticalInside:
                          BorderSide(width: 1.0, color: Colors.black)),
                  children: [
                    buildRow(["Morning", "Afternoon", "Evening", "Undet. time"],
                        isHeader: true),
                    buildRow(["Food 1", "Food 1", "Food 1", "Food 1"]),
                    buildRow(["Food 1", "Food 1", "Food 1", "Food 1"]),
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
                      //defaultColumnWidth: ,
                      // border: TableBorder.all(
                      //     color: Colors.black, style: BorderStyle.solid, width: 1),
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

  List<TableRow> buildAllRowsFood(List<String> array) {
    List<TableRow> rows = [];

    if (array.isEmpty) {
      return [
        buildRow(["None found"])
      ];
    } else if (array.length.remainder(3) != 0) {
      array.add(" ");
    }

    for (var i = 0; i < array.length; i = i + 2) {
      rows.add(buildRow([array[i], array[i + 1]]));
    }
    return rows;
  }
}
