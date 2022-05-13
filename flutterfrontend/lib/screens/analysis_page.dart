import 'package:flutter/material.dart';

class AnalysisPage extends StatefulWidget {
  const AnalysisPage({Key? key}) : super(key: key);

  @override
  State<AnalysisPage> createState() => _AnalysisPageState();
}

class _AnalysisPageState extends State<AnalysisPage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.grey[100],
      body: Padding(
        padding: const EdgeInsets.all(15.0),
        child: Column(children: [
          Row(
            children: [
              Text("Symptoms graph"),
              SizedBox(width: 40.0),
              Icon(Icons.settings, color: Colors.black)
            ],
          ),
          const SizedBox(
            height: 200.0,
            child: Center(
              child: Text("Syptoms graph here"),
            ),
          ),
          Row(
            children: const [
              Text("Food diary"),
              SizedBox(width: 40.0),
              Icon(Icons.settings, color: Colors.black)
            ],
          ),
          Container(
              margin: const EdgeInsets.all(15),
              child: Table(
                  defaultVerticalAlignment: TableCellVerticalAlignment.middle,
                  //defaultColumnWidth: ,
                  // border: TableBorder.all(
                  //     color: Colors.black, style: BorderStyle.solid, width: 1),
                  border: TableBorder(
                      // right: BorderSide(width: 1.0, color: Colors.black),
                      // left: BorderSide(width: 1.0, color: Colors.black),
                      horizontalInside:
                          BorderSide(width: 1.0, color: Colors.black),
                      verticalInside:
                          BorderSide(width: 1.0, color: Colors.black)),
                  children: [
                    TableRow(children: [
                      Column(children: const [
                        Padding(
                          padding: EdgeInsets.all(4.0),
                          child: Text('Morning',
                              style: TextStyle(
                                  fontSize: 16.0, fontWeight: FontWeight.bold)),
                        )
                      ]),
                      Column(children: const [
                        Text('Afternoon',
                            style: TextStyle(
                                fontSize: 16.0, fontWeight: FontWeight.bold))
                      ]),
                      Column(children: const [
                        Text('Evening',
                            style: TextStyle(
                                fontSize: 16.0, fontWeight: FontWeight.bold))
                      ]),
                      Column(children: const [
                        Text('Undet. time',
                            style: TextStyle(
                                fontSize: 16.0, fontWeight: FontWeight.bold))
                      ]),
                    ]),
                    TableRow(children: [
                      Column(children: [
                        Padding(
                          padding: const EdgeInsets.all(4.0),
                          child: Text('Food 1'),
                        )
                      ]),
                      Column(children: [Text('Food 2')]),
                      Column(children: [Text('Food 1')]),
                      Column(children: [Text('Food 1')]),
                    ]),
                    TableRow(children: [
                      Column(children: [
                        Padding(
                          padding: const EdgeInsets.all(4.0),
                          child: Text('Food 1'),
                        )
                      ]),
                      Column(children: [Text('Food 2')]),
                      Column(children: [Text('Food 1')]),
                      Column(children: [Text('Food 1')]),
                    ])
                  ])),
          Row(
            children: [
              Text("Activity log"),
              SizedBox(width: 40.0),
              Icon(Icons.settings, color: Colors.black)
            ],
          ),
          Column(
            children: [
              Padding(
                padding: const EdgeInsets.all(8.0),
                child: Text(
                  'Activities done today',
                  style: TextStyle(fontSize: 16.0, fontWeight: FontWeight.bold),
                ),
              ),
              Padding(
                padding: const EdgeInsets.all(3.0),
                child: Text(
                  'Activity 1',
                ),
              ),
              Padding(
                padding: const EdgeInsets.all(3.0),
                child: Text(
                  'Activity 1',
                ),
              )
            ],
          )
        ]),
      ),
    );
  }
}
