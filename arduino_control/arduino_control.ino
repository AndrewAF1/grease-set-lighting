//greased-lighting
//arduino code 
//written by Andrew Farabow


const int one_RED_PIN = 3;
const int one_GREEN_PIN = 5;
const int one_BLUE_PIN = 6;

const int two_RED_PIN = 9;
const int two_GREEN_PIN = 10;
const int two_BLUE_PIN = 11;

int lNum;

int redVal = 0;
int greenVal = 0;
int blueVal = 0;

bool sIsA = false;


bool oneLooping;
bool oneOn;
long oneStart;
int oneInterval;
int oneRed, oneGreen, oneBlue;
int oneDuration;
long onePrevMillis;
long oneCurrentMillis;



String serialText = "1RGB: 000 000 000";
String two_serialText = "2RGB: 000 000 000";


// the setup function runs once when you press reset or power the board
void setup() {
  pinMode(3, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);

  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);


  Serial.begin(9600);
}

void writeRGB(int num, int red, int green, int blue){

  if (num==1){
    //red
   analogWrite(one_RED_PIN, red);

   //green
   analogWrite(one_GREEN_PIN, green);

   //blue
   analogWrite(one_BLUE_PIN, blue);
  }

  if (num==2){
    //red
   analogWrite(two_RED_PIN, redVal);

   //green
   analogWrite(two_GREEN_PIN, greenVal);

   //blue
   analogWrite(two_BLUE_PIN, blueVal);
  }
   
}

void blinkStep(){
  oneCurrentMillis = millis();
  if (sIsA and serialText.substring(1, 6) == "BLK: "){
    oneLooping = true;
    oneStart = millis();
    oneDuration = serialText.substring(18, 21).toInt()*1000;
    oneInterval = serialText.substring(22, 28).toInt();

    
    oneRed = redVal;
    oneGreen = greenVal;
    oneBlue = blueVal;

    writeRGB(1, 0, 0, 0);
    oneOn = false;

  }

  if (oneLooping and millis()-oneStart >= oneDuration){
    writeRGB(1, 0, 0, 0);
    oneLooping = false;
  }
  else if (oneLooping and (oneCurrentMillis-onePrevMillis >= oneInterval)){

    onePrevMillis = oneCurrentMillis;
    if (!oneOn){
      writeRGB(1, oneRed, oneGreen, oneBlue);
    }
    else if (oneOn){
      writeRGB(1, 0, 0, 0);
    }
    oneOn = !oneOn;
  }
}



// the loop function runs over and over again forever
void loop(){
  sIsA = Serial.available() > 0;
  if (sIsA) {
    
    serialText = Serial.readString();
    serialText.trim();
    
    //Serial.print();

    Serial.println(serialText);

    lNum = serialText.substring(0,1).toInt();

    redVal = serialText.substring(6, 9).toInt();
    greenVal = serialText.substring(10, 13).toInt();
    blueVal = serialText.substring(14, 17).toInt();


    //set color
    if (serialText.substring(1, 6) == "RGB: " && serialText.length() == 17){
      writeRGB(lNum, redVal, greenVal, blueVal);
    }   

    //else {
    //  Serial.println("invalid");
    //}
    
  }

  blinkStep();

   //sIsA = false;
}
