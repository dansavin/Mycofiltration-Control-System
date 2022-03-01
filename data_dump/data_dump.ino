float test_1;
float test_2;

void setup()
{
  Serial.begin(9600);
}

void loop() 
{
  //create test data
  test_1 = (float(random(0,1023))/1024) * 5;
  test_2 = (float(random(0,1023))/1024) * 5;

  //send data to serial
  printSensorData();
  delay(1000);
}

void printSensorData()
{
  //data format:
  //test_1,test_2
  
  Serial.print(test_1,2);
  Serial.print(",");
  Serial.print(test_2,2);
  Serial.println();
}
