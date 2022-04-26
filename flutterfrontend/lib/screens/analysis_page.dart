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
          SizedBox(
            height: 200.0,
            child: Center(
              child: Text("Syptoms graph here"),
            ),
          ),
          Row(
            children: [
              Text("Food diary"),
              SizedBox(width: 40.0),
              Icon(Icons.settings, color: Colors.black)
            ],
          ),
          SizedBox(
            height: 200.0,
            child: Center(
              child: Text("food diary here"),
            ),
          )
        ]),
      ),
    );
  }
}
