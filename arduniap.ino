


const int trigPin = 2;

const int echoPin = 4;



void setup() {


  Serial.begin(9600);

}



void loop()

{


  long duration, inches, centimeters;


  pinMode(trigPin, OUTPUT);

  digitalWrite(trigPin, LOW);

  delayMicroseconds(2);

  digitalWrite(trigPin, HIGH);

  delayMicroseconds(10);

  digitalWrite(trigPin, LOW);

  pinMode(echoPin, INPUT);

  duration = pulseIn(echoPin, HIGH);


  inches = microsecondsToInches(duration);

  centimeters = microsecondsToCentimeters(duration);

  

  Serial.print(inches);

  Serial.print("inches, ");

  Serial.print(centimeters);

  Serial.print("centi meters");

  Serial.println();

  

  delay(10000);

}



long microsecondsToInches(long microseconds)

{

  return microseconds / 74 / 2;

}



long microsecondsToCentimeters(long microseconds)

{
  return microseconds / 29 / 2;

}
