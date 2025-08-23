import React from "react";
import { TrashIcon } from "lucide-react";

interface LitUpButtonProps {
  className?: string;
  text?: string;
  onClick?: () => void;
}

export default function TrashButton({ className, text = "No Text Set", onClick }: LitUpButtonProps) {
  return (
    <div className={`${className || ""}`}>
      <button className={`p-[3px] relative`} onClick={onClick}>
        <div className="absolute inset-0 bg-gradient-to-r from-yellow-500 to-orange-600 rounded-lg" />
        <div className="px-8 py-2  bg-black rounded-[6px]  relative group transition duration-200 text-white hover:bg-orange-900 hover:text-orange-100 flex items-center gap-2">
          <TrashIcon size={16} />
          {text}
        </div>
      </button>
    </div>
  );
}
