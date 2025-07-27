import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from './pages/Home';
import User from './pages/User';
import Developers from "./pages/Developers";

function App() {

  return (
    <>
      <Router>
        <Routes>
          <Route path="/" element={<Home/>} />
          <Route path="/user" element={<User/>} />
          <Route path="/developers" element={<Developers/>} />
        </Routes>
      </Router>
    </>
  )
}

export default App
