<template>
  <div class="space-y-6 h-full flex flex-col">
    <div class="flex items-center justify-between flex-shrink-0">
      <div>
        <h2 class="text-3xl font-bold text-white tracking-tight">1-on-1 Workspace</h2>
        <p class="text-slate-400 mt-1">Collaborate on agendas and track action items</p>
      </div>
      <button class="bg-white/10 hover:bg-white/20 text-white px-5 py-2.5 rounded-xl font-medium transition-colors border border-white/10 flex items-center gap-2">
        <i data-feather="calendar" class="w-4 h-4"></i> Schedule Meeting
      </button>
    </div>

    <div class="flex-1 grid grid-cols-1 lg:grid-cols-4 gap-6 overflow-hidden">
      
      <!-- Meeting List sidebar -->
      <div class="glass-card flex flex-col overflow-hidden">
        <div class="p-4 border-b border-white/5">
          <h3 class="font-semibold text-slate-200">Upcoming & Past</h3>
        </div>
        <div class="flex-1 overflow-y-auto p-2 space-y-1">
          
          <div class="p-3 rounded-lg bg-indigo-500/20 border border-indigo-500/30 cursor-pointer">
            <div class="text-xs text-indigo-300 font-medium mb-1">Today, 3:00 PM</div>
            <div class="font-semibold text-white">Alice Manager</div>
            <div class="text-xs text-slate-400 mt-1 flex items-center gap-1">
              <i data-feather="clock" class="w-3 h-3"></i> 30 mins
            </div>
          </div>

          <div class="p-3 rounded-lg hover:bg-white/5 cursor-pointer transition-colors">
            <div class="text-xs text-slate-400 mb-1">Last Week (Oct 12)</div>
            <div class="font-semibold text-slate-300">Alice Manager</div>
          </div>
          
        </div>
      </div>

      <!-- Main Workspace -->
      <div class="lg:col-span-3 glass-card flex flex-col overflow-hidden">
        
        <div class="p-6 border-b border-white/5 flex items-center justify-between flex-shrink-0">
          <div class="flex items-center gap-4">
            <div class="w-12 h-12 rounded-full bg-gradient-to-tr from-cyan-500 to-blue-500 flex items-center justify-center font-bold text-white">
              AM
            </div>
            <div>
              <h2 class="text-xl font-bold text-white">1-on-1 with Alice</h2>
              <p class="text-sm text-indigo-300">Today, 3:00 PM - 3:30 PM</p>
            </div>
          </div>
          <span class="px-3 py-1 bg-white/5 rounded-full text-xs font-medium text-slate-300 border border-white/10">
            Scheduled
          </span>
        </div>

        <div class="flex-1 overflow-y-auto p-6 space-y-8">
          
          <!-- Shared Agenda -->
          <section>
            <h3 class="text-sm font-semibold text-slate-400 uppercase tracking-wider mb-4 flex items-center gap-2">
              <i data-feather="list" class="w-4 h-4"></i> Shared Agenda
            </h3>
            
            <div class="space-y-3">
              <div class="flex items-start gap-3 group">
                <input type="checkbox" class="mt-1 w-4 h-4 rounded border-slate-600 bg-slate-800 text-indigo-500 focus:ring-indigo-500 focus:ring-offset-slate-900">
                <div class="flex-1">
                  <input type="text" value="Discuss the new dotG architecture plan" class="w-full bg-transparent border-none text-slate-200 focus:ring-0 p-0 text-base placeholder-slate-600" placeholder="Add talking point...">
                </div>
                <button class="text-slate-500 opacity-0 group-hover:opacity-100 transition-opacity hover:text-red-400"><i data-feather="trash-2" class="w-4 h-4"></i></button>
              </div>

              <div class="flex items-start gap-3 group">
                <input type="checkbox" class="mt-1 w-4 h-4 rounded border-slate-600 bg-slate-800 text-indigo-500 focus:ring-indigo-500 focus:ring-offset-slate-900">
                <div class="flex-1">
                  <input type="text" value="Review Q3 OKR progress" class="w-full bg-transparent border-none text-slate-200 focus:ring-0 p-0 text-base placeholder-slate-600" placeholder="Add talking point...">
                </div>
                <button class="text-slate-500 opacity-0 group-hover:opacity-100 transition-opacity hover:text-red-400"><i data-feather="trash-2" class="w-4 h-4"></i></button>
              </div>

              <div class="flex items-center gap-3 pt-2">
                <i data-feather="plus" class="w-4 h-4 text-slate-500 ml-0.5"></i>
                <input type="text" class="flex-1 bg-transparent border-none text-slate-400 focus:ring-0 p-0 text-sm placeholder-slate-600" placeholder="Add new talking point...">
              </div>
            </div>
          </section>

          <!-- Action Items -->
          <section>
            <h3 class="text-sm font-semibold text-slate-400 uppercase tracking-wider mb-4 flex items-center gap-2">
              <i data-feather="check-square" class="w-4 h-4"></i> Action Items
            </h3>
            
            <div class="glass p-4 rounded-xl border border-white/5 space-y-3">
              <div class="flex items-center justify-between text-sm text-slate-300">
                <span>Update the staging environment by EOW</span>
                <span class="px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 text-xs">Carried Over</span>
              </div>
            </div>
          </section>

        </div>
      </div>
      
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import feather from 'feather-icons';

onMounted(() => {
  feather.replace();
});
</script>
