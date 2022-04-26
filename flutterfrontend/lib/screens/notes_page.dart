import 'package:flutter/material.dart';

class Notes extends StatefulWidget {
  const Notes({Key? key}) : super(key: key);

  @override
  State<Notes> createState() => _NotesState();
}

class _NotesState extends State<Notes> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Column(
        children: [
          Center(
            child: CircularProgressIndicator(
              value: 0.5,
              strokeWidth: 20.0,
            ),
          ),
          Text("here is the thing")
        ],
      ),
    );
  }
}
