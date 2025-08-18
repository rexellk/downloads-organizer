import React from 'react';

interface DisplayBoxProps {
  text: string;
  className?: string;
}

const DisplayBox: React.FC<DisplayBoxProps> = ({ text, className = '' }) => {
  return (
    <div className={`display-box ${className}`} style={{
      border: '2px solid #ccc',
      borderRadius: '8px',
      padding: '16px',
      margin: '8px',
      backgroundColor: '#f9f9f9',
      boxShadow: '0 2px 4px rgba(0,0,0,0.1)',
      fontFamily: 'Arial, sans-serif'
    }}>
      {text}
    </div>
  );
};

export default DisplayBox;