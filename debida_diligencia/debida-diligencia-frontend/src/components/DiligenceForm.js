// src/components/DiligenceForm.js
import React, { useState } from 'react';

function DiligenceForm({ onSubmit }) {
    const [companyName, setCompanyName] = useState('');
    const [riskLevel, setRiskLevel] = useState('');
    const [description, setDescription] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        onSubmit({ companyName, riskLevel, description });
    };

    return (
        <div className="diligence-form">
            <h2>Formulario de Análisis de Debida Diligencia</h2>
            <form onSubmit={handleSubmit}>
                <label>Nombre de la Empresa:
                    <input type="text" value={companyName} onChange={(e) => setCompanyName(e.target.value)} />
                </label>
                <label>Nivel de Riesgo:
                    <select value={riskLevel} onChange={(e) => setRiskLevel(e.target.value)}>
                        <option value="">Seleccione</option>
                        <option value="bajo">Bajo</option>
                        <option value="medio">Medio</option>
                        <option value="alto">Alto</option>
                    </select>
                </label>
                <label>Descripción:
                    <textarea value={description} onChange={(e) => setDescription(e.target.value)} />
                </label>
                <button type="submit">Enviar Análisis</button>
            </form>
        </div>
    );
}

export default DiligenceForm;
