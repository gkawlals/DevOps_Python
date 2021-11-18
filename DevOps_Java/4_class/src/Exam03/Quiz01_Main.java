package Exam03;

import java.util.ArrayList;
import java.util.List;

public class Quiz01_Main {
	public void run() {
		// TODO Auto-generated method stub
		Quiz01_Run qr = new Quiz01_Run();
		
		List<Score> score = new ArrayList<Score>();
		
		while(true) {
			
			int menu = qr.menu();
			
			switch(menu) {
				
			case 1:
				Score s = new Score();
				score.add(qr.input(s));
				break;
			case 2:
				qr.output(score);
				System.out.println(score.get(0).getName());
			case 3:
				
				Score findScore = qr.find(score);
				if(findScore != null) {
					qr.update(findScore);
				}else {
					System.out.println("검색한 결과가 없습니다.");
				}
				break;
			case 4:
				Score delScore = qr.find(score);
				if(delScore != null) {
					score.remove(delScore);
					System.out.println("삭제 하였습니다.");
				}else {
					System.out.println("검색한 결과가 없습니다.");
				}
				break;
			case 0:
				System.out.println("프로그램 종료");
				return;
			default:
				System.out.println("메뉴를 잘 못 입력 하셨습니다.\n");
			}
		}
	}
}