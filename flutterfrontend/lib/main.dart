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
      body: IndexedStack(
        index: _selectedIndex,
        children: _screens,
      ),
      bottomNavigationBar: SizedBox(
        height: 70.0,
        child: BottomNavigationBar(
          iconSize: 35,
          items: [
            BottomNavigationBarItem(
                icon: const Icon(Icons.home, color: Colors.black),
                label: "Home",
                backgroundColor: Colors.grey[350]),
            BottomNavigationBarItem(
                icon: const Icon(Icons.calendar_today, color: Colors.black),
                label: "Calendar",
                backgroundColor: Colors.grey[350]),
            BottomNavigationBarItem(
                icon: const Icon(Icons.upload_file, color: Colors.black),
                label: "Upload audio",
                backgroundColor: Colors.grey[350]),
            BottomNavigationBarItem(
                icon: const Icon(Icons.analytics, color: Colors.black),
                label: "Analysis",
                backgroundColor: Colors.grey[350]),
            BottomNavigationBarItem(
                icon: const Icon(Icons.note, color: Colors.black),
                label: "Notes",
                backgroundColor: Colors.grey[350])
          ],
          currentIndex: _selectedIndex,
          selectedItemColor: Colors.black,
          onTap: _onItemTapped,
        ),
      ),
      floatingActionButton: SizedBox(
        height: 70.0,
        width: 70.0,
        child: FloatingActionButton(
          backgroundColor: Colors.green[300],
          onPressed: () {},
          child: const Icon(
            Icons.mic,
            color: Colors.black,
            size: 25,
          ),
        ),
      ),
      floatingActionButtonLocation: FloatingActionButtonLocation.endFloat,
    ));
  }
}
