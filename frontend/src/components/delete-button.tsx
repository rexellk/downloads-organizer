import React from "react";
import { FileWarningIcon } from "lucide-react";


interface LitUpButtonProps {
  className?: string;
  text?: string;
  onClick?: () => void;
}

export default function DeleteButton({ className, text = "No Text Set", onClick }: LitUpButtonProps) {
  return (
    <div className={`${className || ""}`}>
      <button className={`p-[3px] relative`} onClick={onClick}>
        <div className="absolute inset-0 bg-gradient-to-r from-red-600 to-red-800 rounded-lg" />
        <div className="px-8 py-2  bg-black rounded-[6px]  relative group transition duration-200 text-white hover:bg-red-900 hover:text-red-100 flex items-center gap-2">
          <FileWarningIcon size={16} />
          {text}
        </div>
      </button>
    </div>
  );
}
