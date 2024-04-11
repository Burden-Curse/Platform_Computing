//import logo from './logo.svg';
import grad from './image.jpg';
import './App.css';
import ReactDOM from "react-dom";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";

function App() {
  return (
    <Router>
    <header className="App-header">
    <div>
        <meta charSet="UTF-8" />
        <title>About Me</title>
        <link rel="stylesheet" type="text/css" href="Style.css" />
        <nav>
          <a href="https://github.com/Burden-Curse/Platform_Computing" target="_blank" rel="noopener noreferrer">Link to Github</a> &nbsp; &nbsp;
          <Link to="/" target="_blank" rel="noopener noreferrer">Link</Link>
        </nav>
        <h1>About Me</h1>
        <div className="Para1">
        <div class="everything">
          <h2 style={{textAlign: 'center'}}>Early Life</h2>
          <p>
            I was born in Beverly Hills right before New Years (Dec 29).
            We never actually lived near Beverly Hills. I don't know the reason why they were there, all I remember from the conversation was them passing by. After a few days, I was transferred to a cheaper hospital as we couldn't afford the one in Beverly Hills.
            I was a very troublesome kid back in early school. Almost failing 5th grade but I was able to pull through. I have a loving family and very loving grandparents that took care of me. I can visit rarely because they live in Los Angeles
            and try to call as much as I can because of their health.
          </p>
        </div>
        </div>
        <br />
        <br />
        <br />
        <div className="Para2">
          <h2 style={{textAlign: 'center'}}>School and College</h2>
          <p>
            Something that has always stuck with me was something that was I told by my 5th grade teacher and Father. My 5th grade teacher said I wouldn't achieve something in life and my father said I wouldn't make it to college.
            I entered High School and was a very basic student. I couldnt join clubs or stay with friends as I was mostly forced to stay inside. I graduated from Rancho Verde High School with a 2.4 GPA.
            My brother applied me to a community college down the street and they accepted me into a summer program and later a year program called FYE (First Year Experienced). They accepted me because they wanted to give me a second chance as long as I attented
            college full time and did my best. I somehow have ended up being a good student throughout college, although COVID really held me back as I struggled with online. I ended up graduation in 2022 with a 3.4 GPA. 
            It's surprising how well I've done since High School even though I hardly tried at that time only to get a C minimum. 
          </p>
          <img src={grad} alt="Graduation with Grandma" style={{height: 500, width: 500}} />
        </div>
        <br />
        <br />
        <br />
        <div className="Para3">
          <h2 style={{textAlign: 'center'}}>University</h2>
          <p>
            This is my final semester of my 2 years at the University. I recently upgraded from a crappy 2018 Laptop to a beefy 2023 computer as my major is Game Developer. I was cooking that poor laptop trying to work on games for my first year. I've used 3 game
            game engines so far. Unity, Unreal Engine and RenPy. RenPy is more so for a personal project that I've been working on. I want to mainly use Unreal Engine over Unity because of the controversy plus UE being C++. I've somehow have maintained my 3.4 GPA
            somehow through my College and University time.
          </p>
        </div>
        
    </div>
      </header>
    </Router>
  );
}

export default App;


