
          for p_n, count in curr_persona.scratch.chatting_with_buffer.items(): 
            ret_str += f"{p_n}: {count}"

        elif ("print persona associative memory (event)" 
              in sim_command.lower()):
          # Print the associative memory (event) of the persona specified in
          # the prompt
          # Ex: print persona associative memory (event) Isabella Rodriguez
          ret_str += f'{self.personas[" ".join(sim_command.split()[-2:])]}\n'
          ret_str += (self.personas[" ".join(sim_command.split()[-2:])]
                                       .a_mem.get_str_seq_events())

        elif ("print persona associative memory (thought)" 
              in sim_command.lower()): 
          # Print the associative memory (thought) of the persona specified in
          # the prompt
          # Ex: print persona associative memory (thought) Isabella Rodriguez
          ret_str += f'{self.personas[" ".join(sim_command.split()[-2:])]}\n'
          ret_str += (self.personas[" ".join(sim_command.split()[-2:])]
                                       .a_mem.get_str_seq_thoughts())

        elif ("print persona associative memory (chat)" 
              in sim_command.lower()): 
          # Print the associative memory (chat) of the persona specified in
          # the prompt
          # Ex: print persona associative memory (chat) Isabella Rodriguez
          ret_str += f'{self.personas[" ".join(sim_command.split()[-2:])]}\n'
          ret_str += (self.personas[" ".join(sim_command.split()[-2:])]
                                       .a_mem.get_str_seq_chats())

        elif ("print persona spatial memory" 
              in sim_command.lower()): 
          # Print the spatial memory of the persona specified in the prompt
          # Ex: print persona spatial memory Isabella Rodriguez
          self.personas[" ".join(sim_command.split()[-2:])].s_mem.print_tree()

        elif ("print current time" 
              in sim_command[:18].lower()): 
          # Print the current time of the world. 
          # Ex: print current time
          ret_str += f'{self.curr_time.strftime("%B %d, %Y, %H:%M:%S")}\n'
          ret_str += f'steps: {self.step}'

        elif ("print tile event" 
              in sim_command[:16].lower()): 
          # Print the tile events in the tile specified in the prompt 
          # Ex: print tile event 50, 30
          cooordinate = [int(i.strip()) for i in sim_command[16:].split(",")]
          for i in self.maze.access_tile(cooordinate)["events"]: 
            ret_str += f"{i}\n"

        elif ("print tile details" 
              in sim_command.lower()): 
          # Print the tile details of the tile specified in the prompt 
          # Ex: print tile event 50, 30
          cooordinate = [int(i.strip()) for i in sim_command[18:].split(",")]
          for key, val in self.maze.access_tile(cooordinate).items(): 
            ret_str += f"{key}: {val}\n"

        elif ("call -- analysis" 
              in sim_command.lower()): 
          # Starts a stateless chat session with the agent. It does not save 
          # anything to the agent's memory. 
          # Ex: call -- analysis Isabella Rodriguez
          persona_name = sim_command[len("call -- analysis"):].strip() 
          self.personas[persona_name].open_convo_session("analysis")

        elif ("call -- load history" 
              in sim_command.lower()): 
          curr_file = maze_assets_loc + "/" + sim_command[len("call -- load history"):].strip() 
          # call -- load history the_ville/agent_history_init_n3.csv

          rows = read_file_to_list(curr_file, header=True, strip_trail=True)[1]
          clean_whispers = []
          for row in rows: 
            agent_name = row[0].strip() 
            whispers = row[1].split(";")
            whispers = [whisper.strip() for whisper in whispers]
            for whisper in whispers: 
              clean_whispers += [[agent_name, whisper]]

          load_history_via_whisper(self.personas, clean_whispers)

        print (ret_str)

      except:
        traceback.print_exc()
        print ("Error.")
        pass


if __name__ == '__main__':
  # rs = ReverieServer("base_the_ville_isabella_maria_klaus", 
  #                    "July1_the_ville_isabella_maria_klaus-step-3-1")
  # rs = ReverieServer("July1_the_ville_isabella_maria_klaus-step-3-20", 
  #                    "July1_the_ville_isabella_maria_klaus-step-3-21")
  # rs.open_server()

  origin = input("Enter the name of the forked simulation: ").strip()
  target = input("Enter the name of the new simulation: ").strip()

  rs = ReverieServer(origin, target)
  rs.open_server()




















































