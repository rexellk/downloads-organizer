import React, { useState } from "react";
import { createRoot } from "react-dom/client";
import FileInfoCard from "./components/file-info-card";
import AnthropicInfoCard from "./components/anthropic-info-card";
import "./index.css";
import DeleteButton from "./components/delete-button";
import TrashButton from "./components/trash-button";
import { trashCandidates } from "./services/api/api";

const App: React.FC = () => {
  const [trashStatus, setTrashStatus] = useState<string>("");

  const handleTrashClick = async () => {
    const success = await trashCandidates();
    if (success) {
      setTrashStatus("Files moved to trash successfully!");
    } else {
      setTrashStatus("Failed to move files to trash");
    }
    setTimeout(() => setTrashStatus(""), 3000);
  };

  return (
    <div className="min-h-screen bg-black">
      <FileInfoCard className="col-span-3 row-span-1 md:col-span-2 md:row-span-1" />
      <AnthropicInfoCard className="col-span-3 row-span-1 md:col-span-2 md:row-span-1" />
      \
      <div className="flex flex-col justify-center items-center py-2">
                {trashStatus && (
          <div className="pb-2 mt-2 text-white text-sm font-medium">
            {trashStatus}
          </div>
        )}
        <div className="flex justify-center items-center">
          <TrashButton className="px-12" text="Trash Suggestions" onClick={handleTrashClick}/>
          <DeleteButton className="px-12" text="Delete Suggestions"/>
        </div>
      </div>
    </div>
  );
};

const container = document.getElementById("root");
if (container) {
  const root = createRoot(container);
  root.render(<App />);
}
