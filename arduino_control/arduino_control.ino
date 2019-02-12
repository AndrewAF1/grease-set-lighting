//greased-lighting
//arduino code 
//written by Andrew Farabow


const int one_RED_PIN = 3;
const int one_GREEN_PIN = 5;
const int one_BLUE_PIN = 6;

const int two_RED_PIN = 3;
const int two_GREEN_PIN = 5;
const int two_BLUE_PIN = 6;

int one_redVal = 0;
int one_greenVal = 0;
int one_blueVal = 0;

int two_redVal = 0;
int two_greenVal = 0;
int two_blueVal = 0;


String one_serialText = "1RGB: 000 000 000";
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

  //red
  //analogWrite(RED_PIN, 0);

  //green
  //analogWrite(GREEN_PIN, 0);

  //blue
  //analogWrite(BLUE_PIN, 0);

  

}

// the loop function runs over and over again forever
void loop(){
  if (Serial.available() > 0) {
    one_serialText = Serial.readString();
    one_serialText.trim();
    
    //Serial.print();

    Serial.println(one_serialText);

    
    if (one_serialText.substring(0, 6) == "1RGB: " && one_serialText.length() == 17){
       one_redVal = one_serialText.substring(6, 9).toInt();
       one_greenVal = one_serialText.substring(10, 13).toInt();
       one_blueVal = one_serialText.substring(14, 17).toInt();

       //red
       analogWrite(one_RED_PIN, one_redVal);

       //green
       analogWrite(one_GREEN_PIN, one_greenVal);

       //blue
       analogWrite(one_BLUE_PIN, one_blueVal);
      
    }
    else {
      Serial.println("invalid");
    }
  }
}
