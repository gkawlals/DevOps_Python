package If_Eample;

import java.util.Scanner;

public class if_02 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		System.out.println("정수를 입력하세요");
		int num = sc.nextInt();
		
		if ((num % 3) == 0 || (num%5) == 0) {
			System.out.println("조건에 부합합니다");
		}else {
			System.out.println("조건에 부합하지 않습니다.");
		}
	}

}
