package Exam03;

import java.util.List;
import java.util.Scanner;

public class Quiz01_Run {
	Scanner sc = new Scanner(System.in);

	public int menu() {
		System.out.println("=== 메뉴 ===");
		System.out.println("1. 입력");
		System.out.println("2. 출력");
		System.out.println("3. 수정");
		System.out.println("0. 종료");
		System.out.print("입력 : ");
		return sc.nextInt();
	}

	public Score input(Score s) {
		

		System.out.println("이름 입력 : ");
		s.setName(sc.next());
		System.out.println("국어 입력 : ");
		s.setKor(sc.nextInt());
		System.out.println("영어 입력 : ");
		s.setEng(sc.nextInt());
		System.out.println("수학 입력 : ");
		s.setMath(sc.nextInt());


		return s;
	}

	public void output(List<Score> score) {
		for (Score s : score) {
			System.out.println("이름 : " + s.getName() + "\n 국어 점수 : "+ s.getKor() + "\n 영어점수 :" + s.getEng() + "\n 수학점수 :" + s.getMath());
		}

	}

	public Score find(List<Score> score) {
		System.out.println("수정할 이름을 입력해주세요 : ");
		String findName = sc.next();

		for (Score s : score) {
			if (s.getName().equals(findName)) {
				return s;
			}
		}

		return null;

	}

	public void update(Score findScore) {
		System.out.println("수정할 옵션 번호");
		System.out.println("1. 이름");
		System.out.println("2. 국어");
		System.out.println("3. 영어");
		System.out.println("4. 수학");
		System.out.println("0. 돌아가기 ");
		System.out.println("입력 : ");
		
		int menu = sc.nextInt();
		
		switch (menu) {
		case 1:
			System.out.println("수정할 이름 입력 :");
			findScore.setName(sc.next());
			break;
		case 2:
			System.out.println("수정할 국어 점수 입력 :");
			findScore.setKor(sc.nextInt());
		case 3:
			System.out.println("수정할 영어 점수 입력 :");
			findScore.setEng(sc.nextInt());
			break;
		case 4:
			System.out.println("수정할 수학 점수 입력 :");
			findScore.setMath(sc.nextInt());
			break;
		case 0:
			System.out.println("전 메뉴로 돌아가기:");
			break;
		}
		
		
	}




}