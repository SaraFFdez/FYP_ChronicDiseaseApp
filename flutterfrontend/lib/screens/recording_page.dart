import 'package:flutter/material.dart';

class RecordingPage extends StatefulWidget {
  const RecordingPage({Key? key}) : super(key: key);

  @override
  State<RecordingPage> createState() => _RecordingPageState();
}

class _RecordingPageState extends State<RecordingPage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        backgroundColor: Colors.grey[100],
        body: Padding(
          padding: const EdgeInsets.all(15.0),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              const Center(
                  child: Text(
                "Please upload your daily voice recording",
                style: TextStyle(fontSize: 15),
              )),
              const SizedBox(height: 20.0),
              ElevatedButton(
                onPressed: () {},
                child: const Text("Upload"),
              )
            ],
          ),
        ));
  }
}
