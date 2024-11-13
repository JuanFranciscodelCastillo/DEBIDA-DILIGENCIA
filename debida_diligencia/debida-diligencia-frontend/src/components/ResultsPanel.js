// src/components/ResultsPanel.js
import React, { useEffect, useState } from 'react';

function ResultsPanel() {
    const [results, setResults] = useState([]);

    useEffect(() => {
        // Simulación de una llamada API para obtener los datos
        fetch('/api/analisis-resultados')
            .then(response => response.json())
            .then(data => setResults(data))
            .catch(error => console.error('Error fetching results:', error));
    }, []);

    return (
        <div className="results-panel">
            <h2>Panel de Resultados</h2>
            {results.length === 0 ? (
                <p>No hay análisis disponibles.</p>
            ) : (
                <ul>
                    {results.map((result, index) => (
                        <li key={index}>
                            <h3>{result.companyName}</h3>
                            <p><strong>Nivel de Riesgo:</strong> {result.riskLevel}</p>
                            <p><strong>Descripción:</strong> {result.description}</p>
                        </li>
                    ))}
                </ul>
            )}
        </div>
    );
}

export default ResultsPanel;
