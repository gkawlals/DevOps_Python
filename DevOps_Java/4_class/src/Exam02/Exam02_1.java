package Exam02;

public class Exam02_1 {
	public static void main(String[] args) {
		int a = 10;
		int b = 10; 
		
		System.out.println(a == b);
		
		String s1 = "홍길동";
		String s2 = new String("홍길동");
		
		System.out.println(s1 == s2);
		
		System.out.println(s1.equals(s2));
		
	}

}
