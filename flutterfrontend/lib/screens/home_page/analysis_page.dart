import 'package:flutter/material.dart';

class AnalysisPage extends StatefulWidget {
  AnalysisPage({Key? key}) : super(key: key);

  @override
  State<AnalysisPage> createState() => _AnalysisPageState();
}

class _AnalysisPageState extends State<AnalysisPage> {
  @override
  Widget build(BuildContext context) {
    return const Scaffold(
      body: Text("This is the analysis page"),
    );
  }
}
