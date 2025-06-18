import React from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import StudentsView from './pages/StudentsView';

// import './App.css'

function App() {
  return (
    <Router>
      <Routes>
        <Route path= "/" element={<StudentsView />} />
      </Routes>
    </Router>
  );
}

export default App
