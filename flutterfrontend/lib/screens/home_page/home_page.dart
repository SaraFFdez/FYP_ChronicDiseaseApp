import 'package:flutter/material.dart';

class HomePage extends StatefulWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
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
                  child: const Text("TIME"),
                ),
              )
            ],
          ),
          Container(
            padding: const EdgeInsets.fromLTRB(0.0, 200.0, 0.0, 200.0),
            color: Colors.blue,
            child: const Text("Here the progress bar"),
          ),
        ]),
        bottomNavigationBar: BottomNavigationBar(
          items: const [
            BottomNavigationBarItem(
                icon: Icon(Icons.home, color: Colors.black),
                label: "Home",
                backgroundColor: Colors.grey),
            BottomNavigationBarItem(
                icon: Icon(Icons.calendar_today, color: Colors.black),
                label: "Calendar",
                backgroundColor: Colors.grey),
            BottomNavigationBarItem(
                icon: Icon(Icons.mic, color: Colors.black),
                label: "Microphone",
                backgroundColor: Colors.grey),
            BottomNavigationBarItem(
                icon: Icon(Icons.analytics, color: Colors.black),
                label: "Analysis",
                backgroundColor: Colors.grey),
            BottomNavigationBarItem(
                icon: Icon(Icons.note, color: Colors.black),
                label: "Notes",
                backgroundColor: Colors.grey)
          ],
        ));
  }
}
