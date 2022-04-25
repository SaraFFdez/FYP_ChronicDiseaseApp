import 'package:flutter/material.dart';
import 'package:flutterfrontend/screens/analysis_page.dart';
import 'package:flutterfrontend/screens/calendar_page.dart';
import 'package:flutterfrontend/screens//notes_page.dart';
import 'package:flutterfrontend/screens/recording_page.dart';
import 'screens/home_page.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatefulWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  // This widget is the root of your application.
  int _selectedIndex = 0;
  static const List<Widget> _screens = <Widget>[
    HomePage(),
    Calendar(),
    RecordingPage(),
    AnalysisPage(),
    Notes()
  ];

  void _onItemTapped(int index) {
    setState(() {
      _selectedIndex = index;
    });
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        home: Scaffold(
      body: Center(
        child: _screens.elementAt(_selectedIndex),
      ),
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
        currentIndex: _selectedIndex,
        selectedItemColor: Colors.green[400],
        onTap: _onItemTapped,
      ),
    ));
  }
}
