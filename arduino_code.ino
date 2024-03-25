#include <Wire.h>

long accelX, accelY, accelZ;
float gForceX, gForceY, gForceZ;

long gyroX, gyroY, gyroZ;
float rotX, rotY, rotZ;

float AngleRoll, Roll, finalroll, rollpercent;
float AnglePitch, Pitch, finalpitch,finalrollext,rollpercentext;
void setupMPU(){
  Wire.beginTransmission(0b1101000); //This is the I2C address of the MPU (b1101000/b1101001 for AC0 low/high datasheet sec. 9.2)
  Wire.write(0x6B); //Accessing the register 6B - Power Management (Sec. 4.28)
  Wire.write(0b00000000); //Setting SLEEP register to 0. (Required; see Note on p. 9)
  Wire.endTransmission();  
  Wire.beginTransmission(0b1101000); //I2C address of the MPU
  Wire.write(0x1B); //Accessing the register 1B - Gyroscope Configuration (Sec. 4.4) 
  Wire.write(0x00000000); //Setting the gyro to full scale +/- 250deg./s 
  Wire.endTransmission(); 
  Wire.beginTransmission(0b1101000); //I2C address of the MPU
  Wire.write(0x1C); //Accessing the register 1C - Acccelerometer Configuration (Sec. 4.5) 
  Wire.write(0b00000000); //Setting the accel to +/- 2g
  Wire.endTransmission(); 
}

void recordAccelRegisters() {
  Wire.beginTransmission(0b1101000); //I2C address of the MPU
  Wire.write(0x3B); //Starting register for Accel Readings
  Wire.endTransmission();
  Wire.requestFrom(0b1101000,6); //Request Accel Registers (3B - 40)
  while(Wire.available() < 6)
  Serial.println("ahmed");
  accelX = Wire.read()<<8|Wire.read(); //Store first two bytes into accelX
  accelY = Wire.read()<<8|Wire.read(); //Store middle two bytes into accelY
  accelZ = Wire.read()<<8|Wire.read(); //Store last two bytes into accelZ
  processAccelData();
}

void processAccelData(){
  gForceX = (accelX / 16384.0) +0.01;
  gForceY = (accelY / 16384.0) +0.01; 
  gForceZ = (accelZ / 16384.0) +0.04;

  AngleRoll = atan(gForceY/sqrt(gForceX*gForceX+gForceZ*gForceZ))*1/(3.142/180);
  AnglePitch = -atan(gForceX/sqrt(gForceY*gForceY+gForceZ*gForceZ))*1/(3.142/180);

  Roll = map(AngleRoll, -90, 90, 0, 180)  ;
  Pitch = map(AnglePitch, -90, 90, 0, 180)  ;

  finalroll = map(Roll, 170, 25, 0, 180);
  rollpercent = (finalroll/180)*100;

  finalrollext = map(Roll, 170, 120, 0, 180);
  rollpercentext = (finalrollext/180)*100;
}

void recordGyroRegisters() {
  Wire.beginTransmission(0b1101000); //I2C address of the MPU
  Wire.write(0x43); //Starting register for Gyro Readings
  Wire.endTransmission();
  Wire.requestFrom(0b1101000,6); //Request Gyro Registers (43 - 48)
  while(Wire.available() < 6)
  Serial.println("maryam");
  gyroX = Wire.read()<<8|Wire.read(); //Store first two bytes into accelX
  gyroY = Wire.read()<<8|Wire.read(); //Store middle two bytes into accelY
  gyroZ = Wire.read()<<8|Wire.read(); //Store last two bytes into accelZ
  processGyroData();
}

void processGyroData() {
  rotX = gyroX / 131.0;
  rotY = gyroY / 131.0; 
  rotZ = gyroZ / 131.0;
}


#include <LiquidCrystal.h>
//initialise the library with the numbers of the interface pins 
LiquidCrystal lcd(13, 12, 5, 4, 3, 2); 
// declare variables
int sensorpin = A0;  // sensor pin
int sensor;          // sensor readings
int out1 = 10;
int out2 = 9;
int out3 = 8;
int out4 = 7;
auto current = 'c';
void setup() {
  Serial.begin(9600);
  pinMode(out1,INPUT);                   
  pinMode(out2,INPUT);                  
  pinMode(out3,INPUT);                 
  pinMode(out4,INPUT);
  lcd.begin(16, 2); 
  Wire.begin();
  setupMPU();
}

int test =1;
void loop() {
  // put your main code here, to run repeatedly:
  // read sensor value
  sensor = analogRead(sensorpin);
  //Serial.println(sensor);
  auto bol1 = digitalRead(out2) || digitalRead(out3) || digitalRead(out4);
  auto bol2 = digitalRead(out1)  || digitalRead(out3) || digitalRead(out4);
  auto bol3 = digitalRead(out1) || digitalRead(out2) || digitalRead(out4);
  auto bol4 = digitalRead(out1) || digitalRead(out2) || digitalRead(out3);
  // Convert the analog value to resistance
  //float resistance = (1023.0 / sensor) - 1.0;
  lcd.setCursor(0,1);
  if (digitalRead(out1))
    current = 'a'; 
  if (digitalRead(out2))
    current = 'f';  
  if (digitalRead(out3))
    current = 'h';         
if (digitalRead(out1) && !bol1 || current == 'a') 
{   
  //lcd.clear();
  lcd.print("Abduction");
  Serial.println("Abduction");
  lcd.setCursor(0,0);                        
  lcd.print("current option:");          
  Serial.println(finalroll);
  Serial.println(rollpercent);
}
else if (digitalRead(out2) && !bol2 || current == 'f') 
{
  //lcd.clear();
  lcd.print("Flexion");
  Serial.println("Flexion"); 
  lcd.setCursor(0,0);                        
  lcd.print("current option:");         
  Serial.println(finalroll);
  Serial.println(rollpercent);
}
else if (digitalRead(out3) && !bol3 || current == 'h')
{ 
  lcd.print("Hyperextension");
   Serial.println("Hyperextension");
  lcd.setCursor(0,0);                        
  lcd.print("current option:");         
  Serial.println(finalrollext);
  Serial.println(rollpercentext);
}
else if (digitalRead(out4) && !bol4) 
{
  current = 'c';
  lcd.setCursor(0,0);                        
  lcd.print("Please press");
  lcd.setCursor(0,1);  
  lcd.print("other buttons");
}
else if ((digitalRead(out1) && bol1) || (digitalRead(out2) && bol2) || (digitalRead(out3) && bol3) || (digitalRead(out4) && bol4)){   
  lcd.setCursor(0,0); 
  current = 'c';                       
  lcd.print("press only one ");
  lcd.setCursor(0,1);  
  lcd.print("button, please");
}
else if(test > 13)
{
  lcd.setCursor(0,0);                        
  lcd.print("current option:");
}
 delay(2000);
//lcd.clear();
recordAccelRegisters();
recordGyroRegisters();
}

