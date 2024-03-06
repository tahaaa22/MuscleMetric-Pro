// www.sciencebuddies.org

// declare variables
int sensorpin = A0;  // sensor pin
int sensor;          // sensor readings


void setup() {
  // put your setup code here, to run once:
  // set LED pins as outputs
  
  // initialize serial communication
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  // read sensor value
  sensor = analogRead(sensorpin);
  // Convert the analog value to resistance
  //float resistance = (1023.0 / sensor) - 1.0;


  // print sensor value
  Serial.println(sensor);
  // turn on LEDs if sensor reading
  // exceeds a certain threshold
  delay(2000);
}
