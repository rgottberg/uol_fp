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
    // canvas
    element = document.getElementById("recorder");
    var canvas = createCanvas(element.clientWidth, element.clientHeight);
    canvas.parent(element);
    
    // HTML elements    
    var record = document.getElementById("record");

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
// drawing
function draw(){
  // clear canvas to visualize spectrum
  noStroke();
  fill(255,255,255);
  rect(0,10,width,height);
}

// Resize the canvas when the browser's size changes.
function windowResized() {
    resizeCanvas(element.clientWidth, element.clientHeight);

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
    button.innerText = "stop";
    button.style.backgroundColor = "red";
    button.style.color = "white";
  }
  else if (state === 1) {
    // stop recorder and send result to soundFile
    recorder.stop();
    // change state
    state++;
    // style
    button.innerText = "play";
    button.style.backgroundColor = "green";
  }
  else if (state === 2) {
    // play and save recording
    soundfile.play();
    save(soundfile, soundSave); // Saving in downloads - to fix
    // change state
    state = 0;
    // style
    button.innerText = "record";
    button.style.backgroundColor = "lightgrey";
    button.style.color = "black";
  }
}