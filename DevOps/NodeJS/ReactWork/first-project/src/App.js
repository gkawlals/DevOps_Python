import logo from './logo.svg';
import './App.css';

function App() {
  let titles = "방배 소고기 맛집";

  function 함수(){
    return 1400;
  }

  return (
    <div className="App">
      <header className="App-header">
       <div style={{color:'blue', fontSize:'20px'}}> 
        홈페이지 개발
      </div>
       <h4> {titles} </h4>
       <h4> {함수()} </h4>
       <img src={logo}></img>
      </header>
    </div>
  );
}

export default App;
