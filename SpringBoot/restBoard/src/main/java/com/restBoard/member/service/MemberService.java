package com.restBoard.member.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.restBoard.member.dao.MemberDAO;
import com.restBoard.member.vo.MemberVO;

@Service
public class MemberService {
	
	@Autowired
	MemberDAO dao;

	public boolean joinMember(MemberVO vo) {
		
		int cnt = dao.idCheck(vo.getUser_id());
		
		if(cnt == 0) {
			dao.joinMember(vo);
			return true;
		}else {
			return false;
		}
		
		
		
	}

	public int loginCheck(MemberVO vo) {
		return dao.loginCheck(vo);
		
	}

}