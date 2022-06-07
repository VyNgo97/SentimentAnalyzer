import './App.css';
import fetchMovieData from './network/movies';
import Button from '@mui/material/Button'

const App = () => {
  const name = 'Vy';
  const isNameShowing = true;
  return (
    <div className="App">
          {/* surrounding stuff in curly braces executes it as js code */}
          <h1>Hello, {isNameShowing ? name: 'world'}!</h1>
          <Button variant="contained" onClick={fetchMovieData}>Submit</Button>
    </div>
  );
}

export default App;
