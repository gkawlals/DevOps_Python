package Java_test;

import java.util.Scanner;

public class IndexValueAdd {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("정수를 입력해주세요 ");
		int index = sc.nextInt();
		
		int tot = 0;
		while (index > 0) {
			tot += index % 10;
			index /= 10;
		}
		System.out.println(tot);
	}

}
