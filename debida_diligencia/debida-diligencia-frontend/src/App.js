// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './components/Home';
import DiligenceForm from './components/DiligenceForm';
import ResultsPanel from './components/ResultsPanel';

function App() {
    return (
        <Router>
            <div className="app">
                <Routes>
                    <Route path="/" element={<Home />} />
                    <Route path="/formulario-diligencia" element={<DiligenceForm onSubmit={(data) => console.log('Data submitted:', data)} />} />
                    <Route path="/resultados" element={<ResultsPanel />} />
                </Routes>
            </div>
        </Router>
    );
}

export default App;
