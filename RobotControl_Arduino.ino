int a,b,c,d, p=9,q=12,r=4,s=6;
char data;

//a(1),b(2)->right motor ; 1->back
//c(3),d(4)->left motor ; 4->back

void setup()
{
  Serial.begin(9600); //intialising the serial communication 
  pinMode(p,OUTPUT); //pinMode function is used for intialising the pins used
  pinMode(q,OUTPUT); //format is like this->pinMode(pin_number,state)
  pinMode(r,OUTPUT); //state is either OUPUT or INPUT
  pinMode(s,OUTPUT);
}

void loop()
{
  if(Serial.available()>0) //if serial data is being sent
  {
    data = Serial.read(); //assign the coming data to 'data' character
  }
  
// now comparing the data
  if(data == 'f')
  {
    a=1;
    b=0;
    c=1;
    d=0;
    update(a,b,c,d);
  }
  if(data == 'b')
  {
    a=0;
    b=1;
    c=0;
    d=1;
    update(a,b,c,d);
  }
  if(data == 'r')
  {
    a=0;
    b=0;
    c=1;
    d=0;
    update(a,b,c,d);
  }
  if(data == 'l')
  {
    a=1;
    b=0;
    c=0;
    d=0;
    update(a,b,c,d);
  }
  if(data == 's')
  {
    a=0;
    b=0;
    c=0;
    d=0;
    update(a,b,c,d);
  }
}



void update(int a, int b, int c, int d)
{
  digitalWrite(p,b); //digitalWrite is function used to make a pin HIGH or LOW
  digitalWrite(q,a); //format is like this->digitalWrite(pin_number,boolean_state);
  digitalWrite(r,c);
  digitalWrite(s,d);
}