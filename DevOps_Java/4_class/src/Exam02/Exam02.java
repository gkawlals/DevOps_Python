package Exam02;

import java.util.ArrayList;
import java.util.List;

public class Exam02 {
	public static void main(String[] args) {
		List<Score> li = new ArrayList<Score>();
		
		Score s = new Score();
		
		s.setName("홍길동");
		s.setKor(100);
		s.setEng(100);
		s.setMath(100);
		
		li.add(s);
		
		s = new Score();
		
		s.setName("이순신");
		s.setKor(100);
		s.setEng(100);
		s.setMath(100);
		
		li.add(s);
		
		
		
		System.out.println(li.get(0).getName());
		System.out.println(li.get(1).getName());
		System.out.println();
		System.out.println(s.toString());
		System.out.println(s);
		
		
		
	}
}
