<template>
  <div class="space-y-6">
    <div class="flex items-center justify-between">
      <div>
        <h2 class="text-3xl font-bold text-white tracking-tight">Continuous Feedback</h2>
        <p class="text-slate-400 mt-1">Recognize peers and provide nudges</p>
      </div>
      <button class="bg-indigo-500 hover:bg-indigo-600 text-white px-5 py-2.5 rounded-xl font-medium transition-colors shadow-lg shadow-indigo-500/30 flex items-center gap-2">
        <i data-feather="edit-3" class="w-4 h-4"></i> Give Feedback
      </button>
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
      
      <!-- Feed List -->
      <div class="lg:col-span-2 space-y-4">
        
        <div class="glass-card p-5 flex gap-4">
          <div class="w-12 h-12 rounded-full bg-gradient-to-br from-green-400 to-emerald-600 flex-shrink-0 flex items-center justify-center font-bold text-white shadow-lg">
            JD
          </div>
          <div class="flex-1">
            <div class="flex items-center justify-between">
              <h4 class="font-semibold text-white">John Doe <span class="text-slate-400 font-normal text-sm ml-2">to</span> Sawan Parihar</h4>
              <span class="text-xs text-slate-500">2 hours ago</span>
            </div>
            <div class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-md bg-green-500/10 text-green-400 text-xs font-medium mt-2">
              <i data-feather="award" class="w-3.5 h-3.5"></i> Shout-out
            </div>
            <p class="text-slate-300 mt-3 text-sm leading-relaxed">
              Incredible work on the Frappe integration over the weekend! You really pushed the boundaries of what we could deliver for the client. Thank you! 🚀
            </p>
          </div>
        </div>

        <div class="glass-card p-5 flex gap-4">
          <div class="w-12 h-12 rounded-full bg-gradient-to-br from-amber-400 to-orange-600 flex-shrink-0 flex items-center justify-center font-bold text-white shadow-lg">
            AM
          </div>
          <div class="flex-1">
            <div class="flex items-center justify-between">
              <h4 class="font-semibold text-white">Alice Manager <span class="text-slate-400 font-normal text-sm ml-2">to</span> Sawan Parihar</h4>
              <span class="text-xs text-slate-500">Yesterday</span>
            </div>
            <div class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-md bg-amber-500/10 text-amber-400 text-xs font-medium mt-2">
              <i data-feather="target" class="w-3.5 h-3.5"></i> Constructive
            </div>
            <p class="text-slate-300 mt-3 text-sm leading-relaxed">
              Your code quality is great, but let's try to improve the PR descriptions so the QA team has more context before they start testing.
            </p>
            <!-- AI Sentiment Tag -->
            <div class="mt-4 flex items-center gap-2">
              <span class="text-[10px] uppercase tracking-wider text-slate-500 font-semibold">AI Sentiment</span>
              <span class="w-2 h-2 rounded-full bg-yellow-500"></span>
            </div>
          </div>
        </div>

      </div>

      <!-- Quick Actions / Stats -->
      <div class="space-y-6">
        <div class="glass-card p-6 bg-gradient-to-b from-white/5 to-transparent">
          <h3 class="text-sm font-semibold text-slate-400 uppercase tracking-wider mb-4">Your Feedback Stats</h3>
          <div class="space-y-4">
            <div>
              <div class="flex justify-between text-sm mb-1">
                <span class="text-slate-300">Shout-outs Received</span>
                <span class="text-white font-bold">12</span>
              </div>
              <div class="w-full bg-white/5 h-1.5 rounded-full overflow-hidden">
                <div class="bg-green-400 h-full w-[80%] rounded-full"></div>
              </div>
            </div>
            <div>
              <div class="flex justify-between text-sm mb-1">
                <span class="text-slate-300">Constructive</span>
                <span class="text-white font-bold">3</span>
              </div>
              <div class="w-full bg-white/5 h-1.5 rounded-full overflow-hidden">
                <div class="bg-amber-400 h-full w-[20%] rounded-full"></div>
              </div>
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
