# One cool feature is PWM (http://arduino.cc/en/Reference/AnalogWrite) 
# You could use PWM to make the led intensity proportional to the tilt (after the threshold).

void loop(){
	int intensity = 0;
	Yval = analogRead(accPin);
	// Serial.print(“\nY-val: “);
	if (Yval > 580){
		analogWrite(led, 0);
	};
	if (Yval < 480){
		intensity = 127 + (128 * (480 - Yval))/ 480;
		analogWrite(led, intensity);
	};
	// Serial.print(Yval);
	delay(100);
}
