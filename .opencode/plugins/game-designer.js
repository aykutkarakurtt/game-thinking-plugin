/**
 * game-thinking-plugin — OpenCode Plugin
 *
 * Automatically registers:
 * 1. Primary Agent: `game-designer` (from .opencode/agents/game-designer.md)
 * 2. Slash Command: `/analyze` (from .opencode/commands/analyze.md)
 * 3. Bundled Skills: `skills/<skill-name>/SKILL.md`
 * 4. Instructions: `AGENTS.md`
 */

import path from 'path';
import fs from 'fs';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const pluginRootDir = path.resolve(__dirname, '../..');
const agentsDir = path.resolve(__dirname, '../agents');
const commandsDir = path.resolve(__dirname, '../commands');
const skillsDir = path.resolve(pluginRootDir, 'skills');
const instructionsPath = path.resolve(pluginRootDir, 'AGENTS.md');

const parseMarkdownWithFrontmatter = (rawContent) => {
  const match = rawContent.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n?([\s\S]*)$/);
  if (!match) return { frontmatter: {}, body: rawContent.trim() };

  const frontmatter = {};
  for (const rawLine of match[1].split('\n')) {
    const line = rawLine.replace(/\r$/, '');
    const colonIdx = line.indexOf(':');
    if (colonIdx > 0 && !/^\s/.test(line)) {
      const key = line.slice(0, colonIdx).trim();
      const value = line.slice(colonIdx + 1).trim().replace(/^(["'])([\s\S]*)\1$/, '$2');
      frontmatter[key] = value;
    }
  }

  return { frontmatter, body: match[2].trim() };
};

export const GameDesignerPlugin = async () => {
  return {
    config: async (config) => {
      // 1. Register AGENTS.md instructions
      if (fs.existsSync(instructionsPath)) {
        config.instructions = Array.isArray(config.instructions) ? config.instructions : [];
        if (!config.instructions.includes(instructionsPath) && !config.instructions.includes('AGENTS.md')) {
          config.instructions.push(instructionsPath);
        }
      }

      // 2. Register `game-designer` agent from .opencode/agents/game-designer.md
      const agentFile = path.join(agentsDir, 'game-designer.md');
      if (fs.existsSync(agentFile)) {
        const { frontmatter, body } = parseMarkdownWithFrontmatter(fs.readFileSync(agentFile, 'utf8'));
        config.agent = config.agent || {};
        config.agent['game-designer'] = {
          description: frontmatter.description || 'Autonomous Game Design, Market & Thinking Lead for 2D Hyper-Casual / Casual games.',
          mode: frontmatter.mode || 'primary',
          prompt: body,
          ...(config.agent['game-designer'] || {}),
        };

        if (!config.default_agent) {
          config.default_agent = 'game-designer';
        }
      }

      // 3. Register `/analyze` command from .opencode/commands/analyze.md
      const commandFile = path.join(commandsDir, 'analyze.md');
      if (fs.existsSync(commandFile)) {
        const { frontmatter, body } = parseMarkdownWithFrontmatter(fs.readFileSync(commandFile, 'utf8'));
        config.command = config.command || {};
        config.command['analyze'] = {
          description: frontmatter.description || 'Interactive Brainstorm-First game thinking workflow.',
          agent: frontmatter.agent || 'game-designer',
          template: body,
          ...(config.command['analyze'] || {}),
        };
      }

      // 4. Register bundled `skills` directory
      if (fs.existsSync(skillsDir)) {
        config.skills = config.skills || {};
        config.skills.paths = Array.isArray(config.skills.paths) ? config.skills.paths : [];
        if (!config.skills.paths.includes(skillsDir) && !config.skills.paths.includes('skills')) {
          config.skills.paths.push(skillsDir);
        }
      }
    },
  };
};

export default GameDesignerPlugin;
