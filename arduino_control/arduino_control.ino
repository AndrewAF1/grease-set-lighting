//greased-lighting
//arduino code 
//written by Andrew Farabow


const int RED_PIN = 3;
const int GREEN_PIN = 5;
const int BLUE_PIN = 10;

int redVal = 0;
int greenVal = 0;
int blueVal = 0;

String serialBytes = "RGB: 000 000 000";


// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(3, OUTPUT);

  Serial.begin(9600);

  //red
  //analogWrite(RED_PIN, 0);

  //green
  //analogWrite(GREEN_PIN, 0);

  //blue
  //analogWrite(BLUE_PIN, 255);

  

}

// the loop function runs over and over again forever
void loop(){
  if (Serial.available() > 0) {
    serialBytes = Serial.readString();
    
    //Serial.print();

    Serial.println(serialBytes);

    
    if (serialBytes.substring(0, 5) == "RGB: " && serialBytes.length() == 17){
       redVal = serialBytes.substring(5, 8).toInt();
       greenVal = serialBytes.substring(9, 12).toInt();
       blueVal = serialBytes.substring(13, 16).toInt();

       //red
       analogWrite(RED_PIN, redVal);

       //green
       analogWrite(GREEN_PIN, greenVal);

       //blue
       analogWrite(BLUE_PIN, blueVal);
      
    }
    else {
      Serial.println("invalid");
    }
  }
}
