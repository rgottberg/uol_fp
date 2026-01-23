//#!/usr/bin/env python3
//# -*- coding: utf-8 -*-
//"""
//Created on Tue Jan 20 11:58:51 2026
//
//@author: cod
//"
// array for playback buttons
var buttons = [];

// variables for audio recording
var mic;
var recorder;
var user_prompt;
var state=0;

// variable for pre-recorded SoundFile object
var preRecordedSound;

// preload pre-recorded SoundFile
function preload(){
  //soundFormats('mp3', 'wav');
  preRecordedSound = loadSound(soundTest);
}

// initialization
function setup(){   
    // HTML elements    
    var record = document.getElementById("record");
    //var generate = document.getElementById("generate");

    // create an audio in
    mic = new p5.AudioIn();
    
    // prompts user to enable their browser mic
    mic.start();
    
    // create a sound recorder
    recorder = new p5.SoundRecorder();
    
    // connect the mic to the recorder
    recorder.setInput(mic);

    // this sound file will be used to playback & save the recording
    user_prompt = new p5.SoundFile();
    
    // event listeners
    record.addEventListener("click", () => {recordSound(recorder,user_prompt,record)});

}
// record
function recordSound(recorder,soundfile,button){
  // ensure audio is enabled
  userStartAudio();
  // make sure user enabled the mic
  if (state === 0 && mic.enabled) {
    // record to our p5.SoundFile
    recorder.record(soundfile);
    // change state
    state++;
    // style
    button.innerText = "Stop";
    button.style.backgroundColor = "#222222";
  }
  else if (state === 1) {
    // stop recorder and send result to soundFile
    recorder.stop();
    // change state
    state++;
    // style
    button.innerText = "Play";
    button.style.backgroundColor = "green";
  }
  else if (state === 2) {
    // play and save recording
    soundfile.play();
    save(soundfile, soundSave); // Saving in downloads - to fix
    // change state
    state = 0;
    // style
    button.innerText = "Record";
    button.style.backgroundColor = "red";
  }
}