<template>
  <div class="space-y-8">
    <div class="flex items-center justify-between">
      <div>
        <h2 class="text-3xl font-bold text-white tracking-tight">Welcome back, Sawan 👋</h2>
        <p class="text-slate-400 mt-1">Here's what's happening with your performance and growth.</p>
      </div>
      <div class="text-right">
        <p class="text-sm font-medium text-slate-400">Current Cycle</p>
        <p class="text-lg font-bold text-indigo-400">Q2 2026 Appraisal</p>
      </div>
    </div>

    <!-- Quick Stats Grid -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
      
      <!-- OKR Stat -->
      <div class="glass-card p-6 border-l-4 border-indigo-500 relative overflow-hidden group">
        <div class="absolute top-0 right-0 -mt-4 -mr-4 w-24 h-24 bg-indigo-500/20 rounded-full blur-xl group-hover:bg-indigo-500/30 transition-colors"></div>
        <div class="flex items-start justify-between relative z-10">
          <div>
            <p class="text-sm font-medium text-slate-400">OKR Progress</p>
            <h3 class="text-3xl font-bold text-white mt-1">68%</h3>
          </div>
          <div class="w-10 h-10 rounded-xl bg-indigo-500/20 flex items-center justify-center text-indigo-400">
            <i data-feather="target" class="w-5 h-5"></i>
          </div>
        </div>
        <div class="mt-4 flex items-center gap-2 text-sm">
          <span class="text-emerald-400 flex items-center font-medium"><i data-feather="trending-up" class="w-3 h-3 mr-1"></i> +5%</span>
          <span class="text-slate-500">from last week</span>
        </div>
      </div>

      <!-- Feedback Stat -->
      <div class="glass-card p-6 border-l-4 border-emerald-500 relative overflow-hidden group">
        <div class="absolute top-0 right-0 -mt-4 -mr-4 w-24 h-24 bg-emerald-500/20 rounded-full blur-xl group-hover:bg-emerald-500/30 transition-colors"></div>
        <div class="flex items-start justify-between relative z-10">
          <div>
            <p class="text-sm font-medium text-slate-400">Recent Shout-outs</p>
            <h3 class="text-3xl font-bold text-white mt-1">12</h3>
          </div>
          <div class="w-10 h-10 rounded-xl bg-emerald-500/20 flex items-center justify-center text-emerald-400">
            <i data-feather="award" class="w-5 h-5"></i>
          </div>
        </div>
        <div class="mt-4 flex items-center gap-2 text-sm">
          <span class="text-emerald-400 flex items-center font-medium"><i data-feather="trending-up" class="w-3 h-3 mr-1"></i> 2 new</span>
          <span class="text-slate-500">this month</span>
        </div>
      </div>

      <!-- 1on1 Stat -->
      <div class="glass-card p-6 border-l-4 border-amber-500 relative overflow-hidden group">
        <div class="absolute top-0 right-0 -mt-4 -mr-4 w-24 h-24 bg-amber-500/20 rounded-full blur-xl group-hover:bg-amber-500/30 transition-colors"></div>
        <div class="flex items-start justify-between relative z-10">
          <div>
            <p class="text-sm font-medium text-slate-400">Next 1-on-1</p>
            <h3 class="text-xl font-bold text-white mt-1">Today, 3:00 PM</h3>
          </div>
          <div class="w-10 h-10 rounded-xl bg-amber-500/20 flex items-center justify-center text-amber-400">
            <i data-feather="calendar" class="w-5 h-5"></i>
          </div>
        </div>
        <div class="mt-4 flex items-center gap-2 text-sm">
          <span class="text-amber-400 flex items-center font-medium"><i data-feather="alert-circle" class="w-3 h-3 mr-1"></i> Action needed</span>
          <span class="text-slate-500">2 pending items</span>
        </div>
      </div>

    </div>

    <!-- Main Content Grid -->
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
      
      <!-- Action Items Widget -->
      <div class="glass-card p-6">
        <div class="flex items-center justify-between mb-6">
          <h3 class="text-lg font-bold text-white">Pending Action Items</h3>
          <router-link to="/1on1" class="text-sm font-medium text-indigo-400 hover:text-indigo-300">View All</router-link>
        </div>
        
        <div class="space-y-4">
          <div class="flex items-start gap-3 group">
            <input type="checkbox" class="mt-1 w-4 h-4 rounded border-slate-600 bg-slate-800 text-indigo-500 focus:ring-indigo-500 focus:ring-offset-slate-900 cursor-pointer">
            <div class="flex-1">
              <p class="text-sm font-medium text-slate-200 group-hover:text-white transition-colors">Complete Frappe Integration Doc</p>
              <p class="text-xs text-slate-500 mt-1">From 1-on-1 on Oct 12</p>
            </div>
            <span class="px-2 py-0.5 rounded bg-red-500/10 text-red-400 text-xs font-medium border border-red-500/20">Overdue</span>
          </div>

          <div class="flex items-start gap-3 group">
            <input type="checkbox" class="mt-1 w-4 h-4 rounded border-slate-600 bg-slate-800 text-indigo-500 focus:ring-indigo-500 focus:ring-offset-slate-900 cursor-pointer">
            <div class="flex-1">
              <p class="text-sm font-medium text-slate-200 group-hover:text-white transition-colors">Update Q2 OKRs in dotG</p>
              <p class="text-xs text-slate-500 mt-1">From 1-on-1 on Oct 19</p>
            </div>
            <span class="px-2 py-0.5 rounded bg-amber-500/10 text-amber-400 text-xs font-medium border border-amber-500/20">Due Today</span>
          </div>
        </div>
      </div>

      <!-- Recent Feedback Widget -->
      <div class="glass-card p-6">
        <div class="flex items-center justify-between mb-6">
          <h3 class="text-lg font-bold text-white">Recent Feedback</h3>
          <router-link to="/feedback" class="text-sm font-medium text-indigo-400 hover:text-indigo-300">Give Feedback</router-link>
        </div>

        <div class="space-y-4">
          <div class="flex gap-4 p-3 rounded-xl hover:bg-white/5 transition-colors cursor-pointer">
            <div class="w-10 h-10 rounded-full bg-gradient-to-br from-green-400 to-emerald-600 flex-shrink-0 flex items-center justify-center font-bold text-white text-sm">
              JD
            </div>
            <div class="flex-1">
              <div class="flex justify-between items-start">
                <p class="text-sm font-medium text-white">John Doe</p>
                <span class="text-xs text-slate-500">2h ago</span>
              </div>
              <p class="text-sm text-slate-300 mt-1 line-clamp-2">Incredible work on the Frappe integration over the weekend! You really pushed...</p>
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
