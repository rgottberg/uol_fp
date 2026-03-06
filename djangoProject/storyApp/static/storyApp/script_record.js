// array for playback buttons
var buttons = [];

// variables for audio recording
var mic;
var recorder;
var user_prompt;
var state=0;
var soundBlob; 

// initialization
function setup(){
    noCanvas()   
    // HTML elements    
    var record = document.getElementById("btn_record");
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
    button.innerText = "Stop your recording";
    button.style.backgroundColor = "#222222";
  }
  else if (state === 1) {
    // stop recorder and send result to soundFile
    recorder.stop();
    // change state
    state++;
    // style
    button.innerText = "Play your recording";
    button.style.backgroundColor = "green";
  }
  else if (state === 2) {
    // play and save recording
    soundfile.play();
    // audio data blob
    soundBlob = soundfile.getBlob();
    sendBlob(soundBlob)
    // change state
    state = 0;
    // style
    button.innerText = "Tell me what your story is about ...";
    button.style.backgroundColor = "red";
  }
}

// send blob to server
function sendBlob(soundBlob) {
    var serverUrl = 'http://127.0.0.1:8000/blob/';
    
    var formData = new FormData();
    formData.append('soundBlob', soundBlob);
    
    var httpRequestOptions = {
        method: 'POST',
        body: formData,
        headers: {'X-CSRFToken': csrftoken}
    };
    httpDo(serverUrl, httpRequestOptions);
}

// csrf token
const csrftoken = getCookie('csrftoken');

// Django's documentation: acquiring csrf token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}