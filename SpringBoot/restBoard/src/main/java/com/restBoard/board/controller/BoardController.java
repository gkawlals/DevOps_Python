package com.restBoard.board.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

import com.restBoard.board.service.BoardService;
import com.restBoard.board.vo.BoardVO;

@Controller
@RequestMapping("board")
public class BoardController {
	@Autowired
	BoardService service;
	
	@RequestMapping("boardList")
	public String boardList(Model model) {
		List<BoardVO> boardList = service.selectList();
		model.addAttribute("boardList", boardList);
		return "board/boardList";
	}
	
	@RequestMapping(value="insertBoard", method=RequestMethod.GET)
	public String insertBoard() {
		return "board/insertBoard";
	}
	
	@RequestMapping(value="insertBoard", method=RequestMethod.POST)
	public String insertBoard(BoardVO vo) {
		service.insertBoard(vo);
		return "redirect:boardlist";
	}
	
	@RequestMapping("getBoard")
	public String getBoard(Model model, int seq) {
		BoardVO vo = service.getBoard(seq);	
		model.addAttribute("board", vo);
		return "board/getBoard";
	}
	
	@GetMapping("updateBoard")
	public String updateBoard(Model model, int seq) {
		BoardVO vo = service.updateBoard(seq);	
		model.addAttribute("board", vo);
		return "board/updateBoard";
	}
	
	@PostMapping("updateBoard")
	public String updateBoard(Model model, BoardVO vo) {
		service.updateBoard(vo);
		model.addAttribute("board", vo);
		return "redirect:getBoard?seq="+vo.getSeq();
	
	}
	
	@GetMapping("deleteBoard")
	public String deleteBoard(int seq) {
		service.deleteBoard(seq);
		return "redirect:boardlist";
	}
}