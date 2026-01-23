//#!/usr/bin/env python3
//# -*- coding: utf-8 -*-
//"""
//Created on Tue Jan 20 11:58:51 2026
//
//@author: cod
//"

// pre-recorded SoundFile object (audio story)
var preRecordedSound;

// FFT analyzer
var fft;

var element;

// initialization
function setup(){  
    // canvas
    element = document.getElementById("waveform");
    var canvas = createCanvas(element.clientWidth, element.clientHeight);
    canvas.parent(element);
    
    // HTML elements    
    var pause = document.getElementById("pause");
    var play = document.getElementById("play");
    var stop = document.getElementById("stop");

    // audio story
    preRecordedSound = loadSound(story);

    // event listeners
    pause.addEventListener("click", () => {pauseSound(preRecordedSound)});
    play.addEventListener("click", () => {playSound(preRecordedSound)});
    stop.addEventListener("click", () => {stopSound(preRecordedSound)});
    
    // FFT analyzer
    fft = new p5.FFT(0.2,256);
        
}
// drawing
function draw(){
  // clear canvas to visualize spectrum
  noStroke();
  fill("#222222");
  rect(0,10,width,height);
  
  // FFT analyzer
  push();
    translate(0,height/2);
    fill(0,255,0);
    spectrum(preRecordedSound,fft);
    pop();
}

// Resize the canvas when the browser's size changes.
function windowResized() {
    resizeCanvas(element.clientWidth, element.clientHeight);
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
        vertex(x, h - height/2);
        }
    endShape();
}