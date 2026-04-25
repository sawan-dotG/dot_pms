<template>
  <div class="space-y-6">
    <div class="flex items-center justify-between">
      <div>
        <h2 class="text-3xl font-bold text-white tracking-tight">Objectives & Key Results</h2>
        <p class="text-slate-400 mt-1">Align your goals with the company's vision</p>
      </div>
      <button class="bg-indigo-500 hover:bg-indigo-600 text-white px-5 py-2.5 rounded-xl font-medium transition-colors shadow-lg shadow-indigo-500/30 flex items-center gap-2">
        <i data-feather="plus" class="w-4 h-4"></i> New Objective
      </button>
    </div>

    <!-- OKR Tree View Mockup -->
    <div class="glass-card p-6 space-y-6">
      
      <!-- Objective Item -->
      <div class="bg-slate-800/50 rounded-xl p-5 border border-white/5">
        <div class="flex items-start justify-between">
          <div class="flex-1">
            <div class="flex items-center gap-3 mb-2">
              <span class="px-2.5 py-1 rounded-full bg-indigo-500/20 text-indigo-300 text-xs font-semibold">Company Objective</span>
              <span class="text-slate-400 text-sm"><i data-feather="users" class="w-4 h-4 inline mr-1"></i> Public</span>
            </div>
            <h3 class="text-xl font-semibold text-white">Expand into the European Market</h3>
            <p class="text-slate-400 text-sm mt-1">Owner: CEO</p>
          </div>
          <div class="text-right">
            <div class="text-2xl font-bold text-gradient">65%</div>
            <p class="text-xs text-slate-400">Overall Progress</p>
          </div>
        </div>

        <!-- Key Results -->
        <div class="mt-6 space-y-3">
          
          <div class="glass rounded-lg p-4 flex items-center justify-between group">
            <div class="flex items-center gap-4 flex-1">
              <div class="w-2 h-2 rounded-full bg-green-400"></div>
              <div class="flex-1">
                <p class="font-medium text-slate-200">Close 50 Enterprise Deals in EU</p>
                <div class="w-full bg-slate-700/50 h-1.5 rounded-full mt-2 overflow-hidden">
                  <div class="bg-gradient-to-r from-green-400 to-emerald-400 h-full rounded-full" style="width: 80%"></div>
                </div>
              </div>
            </div>
            <div class="ml-6 text-right">
              <p class="text-sm font-semibold text-white">40 / 50</p>
              <button class="text-xs text-indigo-400 opacity-0 group-hover:opacity-100 transition-opacity">Update Check-in</button>
            </div>
          </div>

          <div class="glass rounded-lg p-4 flex items-center justify-between group">
            <div class="flex items-center gap-4 flex-1">
              <div class="w-2 h-2 rounded-full bg-amber-400"></div>
              <div class="flex-1">
                <p class="font-medium text-slate-200">Hire EU Regional Director</p>
                <div class="w-full bg-slate-700/50 h-1.5 rounded-full mt-2 overflow-hidden">
                  <div class="bg-gradient-to-r from-amber-400 to-orange-400 h-full rounded-full" style="width: 50%"></div>
                </div>
              </div>
            </div>
            <div class="ml-6 text-right">
              <p class="text-sm font-semibold text-white">50%</p>
              <button class="text-xs text-indigo-400 opacity-0 group-hover:opacity-100 transition-opacity">Update Check-in</button>
            </div>
          </div>

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
