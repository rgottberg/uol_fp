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

// variables for FFT analyzer
var fft;

// preload pre-recorded SoundFile
function preload(){
  //soundFormats('mp3', 'wav');
  preRecordedSound = loadSound(soundTest);
}

// initialization
function setup(){

  // create canvas
  createCanvas(300,400);

  // create playback buttons
  buttons = [];
  buttons.push(createButton("pause"));
  buttons.push(createButton("play"));
  buttons.push(createButton("stop"));
  buttons.push(createButton("record"));  
  // style playback buttons
  var buttonWidth = width/buttons.length;
  var buttonHeight = 50;
  for (var i=0;i<buttons.length;i++)
  {
    buttons[i].position(i*buttonWidth,height-(buttonHeight*1.1));
    buttons[i].size(buttonWidth,buttonHeight);
  }
  
  // audio recording /////////////////////////
  // create an audio in
  mic = new p5.AudioIn();
  // prompts user to enable their browser mic
  mic.start();
  // create a sound recorder
  recorder = new p5.SoundRecorder();
  // connect the mic to the recorder
  recorder.setInput(mic);
  // this sound file will be used to
  // playback & save the recording
  user_prompt = new p5.SoundFile();
  
  // call playback functions with mousePressed
  buttons[0].mousePressed(()=>{pauseSound(preRecordedSound)});
  buttons[1].mousePressed(()=>{playSound(preRecordedSound)});
  buttons[2].mousePressed(()=>{stopSound(preRecordedSound)});
  buttons[3].mouseClicked(()=>{recordSound(recorder,user_prompt,buttons[3])});
     
  // FFT analyzer
  fft = new p5.FFT(0.2,256);
}
// drawing
function draw(){
  // clear canvas to visualize spectrum
  noStroke();
  fill(255,255,255);
  rect(0,0,width,height);
  
  // FFT analyzer
  push();
    translate(0,height/2);
    fill(0,255,0);
    spectrum(preRecordedSound,fft);
    pop();
}

// pause
function pauseSound(soundfile){
  if (soundfile.isPlaying()){
    soundfile.pause();
  } 

}
// play
function playSound(soundfile){
  if (soundfile.isPlaying()){
    soundfile.stop();
  } 
  soundfile.play();

}
// stop
function stopSound(soundfile){
  if (soundfile.isPlaying()){
    soundfile.stop();
  } 
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
    button.html("stop");
    button.style('background-color', "red");
    button.style('color', "white");
  }
  else if (state === 1) {
    // stop recorder and send result to soundFile
    recorder.stop();
    // change state
    state++;
    // style
    button.html("play");
    button.style('background-color', "green");
  }
  else if (state === 2) {
    // play and save recording
    soundfile.play();
    save(soundfile, soundSave); // Saving in downloads - to fix
    // change state
    state = 0;
    // style
    button.html("record");
    button.style('background-color', "lightgrey");
    button.style('color', "black");
  }
}

// FFT visualization
function spectrum(soundfile,analyzer){
  //var spect = analyzer.analyze();
  var spect = analyzer.waveform();
  analyzer.setInput(soundfile)
  beginShape();
  for (let i = 0; i < spect.length; i++) {
    let x = map(i, 0, spect.length, 0, width);     
    //let h = -height + map(spect[i], 0, 300, height, 0);
    let h = map(spect[i], -1, 1, height, 0);
    //rect(x, height/3, width/spect.length, h);
    vertex(x, h-height/2);
  }
  endShape();
}
