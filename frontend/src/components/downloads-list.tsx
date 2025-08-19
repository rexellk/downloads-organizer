import React from "react";
import { useState, useEffect } from "react";
import { FileInfo } from "../types/api";
import { fetchFiles } from "../services/api/api";

interface DisplayBoxProps {
  className?: string;
}

const DownloadsList: React.FC<DisplayBoxProps> = ({ className = "" }) => {
  const [files, setFiles] = useState<FileInfo[]>([]);
  const [loading, setLoading] = useState<boolean>(true);

  useEffect(() => {
    const loadFiles = async () => {
      try {
        setLoading(true);
        const data = await fetchFiles();
        setFiles(data.files);
      } catch (error) {
        console.error("Error: ", error);
      } finally {
        setLoading(false);
      }
    };
    loadFiles();
  }, []);

  if (loading) {
    return <div> Loading... </div>;
  }

  return (
    <div
      className={`display-box ${className}`}
      style={{
        border: "2px solid #ccc",
        borderRadius: "8px",
        padding: "16px",
        margin: "8px",
        backgroundColor: "#f9f9f9",
        boxShadow: "0 2px 4px rgba(0,0,0,0.1)",
        fontFamily: "Arial, sans-serif",
      }}
    >
      {files.map((file) => (
        <div key={file.name}>
          <h3>{file.name}</h3>
          <p>{file.size_mb} MB</p>
        </div>
      ))}
    </div>
  );
};

export default DownloadsList;
