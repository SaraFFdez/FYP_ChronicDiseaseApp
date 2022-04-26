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
  double _progressValue = 0.63;
  double _progressValuePercent = 63.0;

  String getCorrectTime() {
    String minutes = "";
    if (DateTime.now().minute < 10) {
      minutes = "0" + DateTime.now().minute.toString();
    } else {
      minutes = DateTime.now().minute.toString();
    }
    return DateTime.now().hour.toString() + ":" + minutes;
  }

  @override
  void initState() {
    _timeString = getCorrectTime();
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

    String time = getCorrectTime();

    setState(() {
      _timeString = time;
      _dateString = date;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.grey[100],
      body: Column(
          //crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            SizedBox(
              height: 40.0,
              child: Container(
                  decoration: const BoxDecoration(
                      gradient: LinearGradient(
                begin: Alignment.topCenter,
                end: Alignment.bottomCenter,
                colors: [
                  Color.fromARGB(255, 167, 246, 170),
                  Color(0xFFF5F5F5),
                ],
              ))),
            ),
            Expanded(
                flex: 1,
                child: Row(
                  children: [
                    const Expanded(
                      flex: 1,
                      child: SizedBox(),
                    ),
                    Expanded(
                      flex: 3,
                      child: Container(
                        padding: const EdgeInsets.all(20),
                        color: Colors.white,
                        child: Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Text(
                                _timeString,
                                style: const TextStyle(
                                    fontSize: 60), //change the font later
                              ),
                              const SizedBox(height: 10.0),
                              Text(_dateString,
                                  style: const TextStyle(fontSize: 25))
                            ]), //if we find a way to center this in the row, yay
                      ),
                    ),
                  ],
                )),
            Expanded(
                flex: 3,
                child: Row(
                  children: [
                    const Expanded(flex: 1, child: SizedBox()),
                    Expanded(
                        flex: 6,
                        child: SizedBox(
                            height: 350.0,
                            width: 200.0,
                            child: Stack(
                              children: [
                                Center(
                                  child: SizedBox(
                                    height: 320.0,
                                    width: 320.0,
                                    child: CircularProgressIndicator(
                                      value: _progressValue,
                                      backgroundColor: const Color.fromARGB(
                                          255, 119, 118, 118),
                                      valueColor:
                                          const AlwaysStoppedAnimation<Color>(
                                              Colors.green),
                                      strokeWidth: 30.0,
                                    ),
                                  ),
                                ),
                                Center(
                                    child: Text(
                                  "Progress: $_progressValuePercent %",
                                  style: const TextStyle(
                                      fontSize: 30,
                                      fontWeight: FontWeight.bold),
                                ))
                              ],
                            ))),
                    const Expanded(flex: 1, child: SizedBox()),
                  ],
                ))
          ]),
    );
  }
}
