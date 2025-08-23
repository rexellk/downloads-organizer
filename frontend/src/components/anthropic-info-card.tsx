"use client";

import { useState } from "react";
import { motion } from "motion/react";
import { ArrowUpRight } from "lucide-react";
import { FileInfo } from "../types/api";
import { fetchCandidates } from "../services/api/api";

interface FileInfoCardProps {
  className?: string;
}

const AnthropicInfoCard = ({ className }: FileInfoCardProps) => {
  const [candidates, setCandidates] = useState<string[]>([]);
  const [loading, setLoading] = useState(false);

  const handleClick = () => {
    const loadCandidates = async () => {
      try {
        setLoading(true);
        const data = await fetchCandidates();
        // Anthropic API returns just filenames, not full file objects
        setCandidates(data.files || data);
      } catch (error) {
        console.error("Error: ", error);
      } finally {
        setLoading(false);
      }
    };
    loadCandidates();
  };

  const formatCandidatesDisplay = (candidates: string[]) => {
    if (loading) return "Loading deletion suggestions...";
    if (!candidates || candidates.length === 0)
      return "Click to get deletion suggestions...";
    return candidates.map((filename) => `- ${filename}`).join("\n");
  };

  return (
    <div className="px-6 pt-3 pb-0 md:px-8 md:pt-4 md:pb-1 lg:px-12 lg:pt-6 lg:pb-1">
      <motion.div
        whileHover={{ y: -5 }}
        transition={{ type: "spring", stiffness: 300, damping: 20 }}
        className="h-full"
      >
        <div
          onClick={handleClick}
          className={`
                    group relative flex flex-col gap-4 h-full rounded-xl p-5 cursor-pointer
                    bg-gradient-to-b from-neutral-50/60 via-neutral-50/40 to-neutral-50/30 
                    dark:from-neutral-900/60 dark:via-neutral-900/40 dark:to-neutral-900/30
                    border border-neutral-200/60 dark:border-neutral-800/60
                    before:absolute before:inset-0 before:rounded-xl
                    before:bg-gradient-to-b before:from-white/10 before:via-white/20 before:to-transparent 
                    dark:before:from-black/10 dark:before:via-black/20 dark:before:to-transparent
                    before:opacity-100 before:transition-opacity before:duration-500
                    after:absolute after:inset-0 after:rounded-xl after:bg-neutral-50/70 dark:after:bg-neutral-900/70 after:z-[-1]
                    backdrop-blur-[4px]
                    shadow-[0_4px_20px_rgb(0,0,0,0.04)] dark:shadow-[0_4px_20px_rgb(0,0,0,0.2)]
                    hover:border-neutral-300/50 dark:hover:border-neutral-700/50
                    hover:shadow-[0_8px_30px_rgb(0,0,0,0.06)] dark:hover:shadow-[0_8px_30px_rgb(0,0,0,0.3)]
                    hover:backdrop-blur-[6px]
                    hover:bg-gradient-to-b hover:from-neutral-50/60 hover:via-neutral-50/30 hover:to-neutral-50/20
                    dark:hover:from-neutral-800/60 dark:hover:via-neutral-800/30 dark:hover:to-neutral-800/20
                    transition-all duration-500 ease-out ${className}
                `}
          tabIndex={0}
          aria-label="Get downloaded files Info - Tap this bento grid to view all your files in the downloads directory"
        >
          <div
            className="relative z-10 flex flex-col gap-3 h-full"
            style={{ transform: "translateZ(20px)" }}
          >
            <div className="space-y-2 flex-1 flex flex-col">
              <div className="flex items-center justify-between">
                <h3 className="text-xl font-semibold tracking-tight text-neutral-900 dark:text-neutral-100 group-hover:text-neutral-700 dark:group-hover:text-neutral-300 transition-colors duration-300">
                  Get Deletion Suggestions
                </h3>
                <div className="text-neutral-400 dark:text-neutral-500 opacity-0 transition-opacity duration-200 group-hover:opacity-100">
                  <ArrowUpRight className="h-5 w-5" />
                </div>
              </div>

              <p className="text-sm text-neutral-600 dark:text-neutral-400 tracking-tight">
                Use Anthropic API to suggest what files to delete
              </p>

              <div className="mt-4">
                <textarea
                  value={formatCandidatesDisplay(candidates)}
                  readOnly
                  placeholder="Click to get deletion suggestions..."
                  className="w-full p-4 rounded-lg bg-neutral-100/80 dark:bg-neutral-800/80 border border-neutral-200/50 dark:border-neutral-700/50 h-[150px] resize-none text-sm text-neutral-900 dark:text-neutral-100 placeholder-neutral-500 dark:placeholder-neutral-400 focus:outline-none focus:ring-2 focus:ring-emerald-500/50 dark:focus:ring-emerald-400/50 focus:border-emerald-500/50 dark:focus:border-emerald-400/50 transition-all duration-200 read-only:cursor-default overflow-y-auto whitespace-pre-line"
                />
              </div>
            </div>
          </div>
        </div>
      </motion.div>
    </div>
  );
};

export default AnthropicInfoCard;
