import 'package:flutter/material.dart';
import 'dart:async';

class HomePage extends StatefulWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  String _timeString = "00:00";
  String _dateString = "00/00/00";
  late Timer _timer;

  @override
  void initState() {
    _timeString =
        DateTime.now().hour.toString() + ":" + DateTime.now().minute.toString();
    _dateString = DateTime.now().day.toString() +
        "/" +
        DateTime.now().month.toString() +
        "/" +
        DateTime.now().year.toString();
    _timer =
        Timer.periodic(const Duration(seconds: 1), (Timer t) => _getTime());
    super.initState();
  }

  @override
  void dispose() {
    _timer.cancel();
    super.dispose();
  }

  void _getTime() {
    String date = DateTime.now().day.toString() +
        "/" +
        DateTime.now().month.toString() +
        "/" +
        DateTime.now().year.toString();

    String time =
        DateTime.now().hour.toString() + ":" + DateTime.now().minute.toString();

    setState(() {
      _timeString = time;
      _dateString = date;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.grey[100],
      appBar: AppBar(
        title: const Text(
          "My first app",
          style: TextStyle(color: Colors.black),
        ),
        centerTitle: true,
        backgroundColor: Colors.green[100],
      ),
      body: Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
        Row(
          children: [
            const Expanded(
              flex: 1,
              child: SizedBox(),
            ),
            Expanded(
              flex: 3,
              child: Container(
                padding: const EdgeInsets.all(40),
                color: Colors.white,
                child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        _timeString,
                        style: const TextStyle(
                            fontSize: 30), //change the font later
                      ),
                      const SizedBox(height: 5.0),
                      Text(_dateString)
                    ]), //if we find a way to center this in the row, yay
              ),
            ),
          ],
        ),
        Container(
          padding: const EdgeInsets.fromLTRB(0.0, 200.0, 0.0, 200.0),
          color: Colors.blue,
          child: const Text("Here the progress bar"),
        ),
      ]),
    );
  }
}
