
.....................................................................
1. What will happen when you attempt to compile and run the following code?
public class MyField{
String s;
public static void main(String argv[]){
MyField m = new MyField();
m.amethod();
}
void amethod(){
System.out.println(s);
}
}

A. Compile time error s has not been initialised 
B. Runtime error s has not been initialised 
C. Blank output 
D. Output of null 

Answer: Option D
.....................................................................

2. What will be the output of the below code segement:

String[] elements = {"Java","is","platform","independent"};
String result = (elements.length > 0) ? elements[0]:null;
System.out.printf(result);

A. independent 
B. java 
C. is 
D. platform 

Answer: Option B
..........................................................................
3. What will be the output of the below code segement:

public class SwitchTest {
public static void main(String argv[]) {
SwitchTest ms=new SwitchTest();
ms.display();
}
public void display() {
int k=10;
switch(k){

default:
System.out.println("This is the default output");
break;
case 10:
System.out.println("ten");
break;
case 20:
System.out.println("twenty");
break;
}
}
}

A. ten 
B. twenty 
C. ten twenty 
D. None 

Option A

4. Which Exception Will occur

class Test {
public static void main(String[ ] args) {
try {
String s = "5.6";
Integer.parseInt(s); // Cause a NumberFormatException
int i = 0;
int y = 2 / i;
System.out.println("Welcome to Java");
} catch (Exception ex) {
System.out.println(ex);
}
}
}

A. Welcome to Java 
B. NumberFormatException 
C. Exception 
D. None 

Answer: Option B
................................................................
6. Consider the following code. What is the Output:

public class StaticTest {
static {
System.out.println("Planet");
}
public static void main(String argv[]) {
}
static {
System.out.print("Welcome");
}
}

A. Planet 
B. Welcome 
C. Planet Welcome 
D. None 
Answer: Option C

..............................................
8. What is the Output

class ArrayTest {
public static void main(String[] args) {
int[][] a1 = {{1,2,3},{4,5,6},{7,8,9,10}};
System.out.print(a1[0][2]+","+a1[1][0]+","+a1[2][1]);
}
}

A. Prints: 3, 4, 8 
B. Prints: 7, 2, 6 
C. Run-time error 
D. Compile-time error 

Answer: Option A
..................................................

9. What will happen when you try to compile and run this code?

public class TGo implements Runnable{
public static void main(String argv[]){
TGo tg = new TGo();
Thread t = new Thread(tg);
t.start();
}
public void run() {
while(true) {
Thread.currentThread().sleep(1000);
System.out.println("looping while");
}
}
}

A. Compilation and no output 
B. Compilation and repeated output of "looping while" 

Answer: Option B
...........................................
C. Compilation and single output of "looping while" 

......................................
.........................................