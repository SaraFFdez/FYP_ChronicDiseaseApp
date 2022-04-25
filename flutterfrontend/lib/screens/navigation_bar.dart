import 'package:flutter/material.dart';

class NavigationBar extends StatefulWidget {
  const NavigationBar({Key? key}) : super(key: key);

  @override
  State<NavigationBar> createState() => _NavigationBarState();
}

//Esto luego lo llaman en el body https://api.flutter.dev/flutter/material/BottomNavigationBar-class.html
//They push the different bodys in. I wonder if we could push scaffolds?
//Icon sizes and font can also be modified
//https://www.youtube.com/watch?v=xoKqQjSDZ60&ab_channel=JohannesMilke
class _NavigationBarState extends State<NavigationBar> {
  int _selectedIndex = 0;
  static const TextStyle optionStyle =
      TextStyle(fontSize: 30, fontWeight: FontWeight.bold);
  static const List<Widget> _screens = <Widget>[
    Text(
      'Index 0: Home',
      style: optionStyle,
    ),
    Text(
      'Index 1: Business',
      style: optionStyle,
    ),
    Text(
      'Index 2: School',
      style: optionStyle,
    ),
  ];

  void _onItemTapped(int index) {
    setState(() {
      _selectedIndex = index;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
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
    );
  }
}
